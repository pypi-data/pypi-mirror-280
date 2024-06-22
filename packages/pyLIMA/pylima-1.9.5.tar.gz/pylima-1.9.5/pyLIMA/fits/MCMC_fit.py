import sys
import time as python_time

import emcee
import numpy as np
from pyLIMA.fits.ML_fit import MLfit
from pyLIMA.priors import parameters_priors

class MCMCfit(MLfit):
    """
    Monte-Carlo Markov Chain using emcee
    https://emcee.readthedocs.io/en/stable/

    Attributes
    -----------
    MCMC_walkers : int, the number of walkers = number_of_walkers*len(fit_parameters)
    MCMC_links : int, the total number of iteration
    """
    def __init__(self, model, rescale_photometry=False, rescale_astrometry=False,
                 telescopes_fluxes_method='polyfit', loss_function='likelihood',
                 MCMC_walkers=2, MCMC_links=5000):
        """The fit class has to be intialized with an event object."""

        super().__init__(model, rescale_photometry=rescale_photometry,
                         rescale_astrometry=rescale_astrometry,
                         telescopes_fluxes_method=telescopes_fluxes_method,
                         loss_function=loss_function)

        self.MCMC_walkers = MCMC_walkers  # times number of dimension!
        self.MCMC_links = MCMC_links

    def fit_type(self):
        return "Monte Carlo Markov Chain (Affine Invariant)"

    def objective_function(self, fit_process_parameters):

        #if self.loss_function != 'likelihood':

        limits_check = self.fit_parameters_inside_limits(fit_process_parameters)

        if limits_check is not None:

            return -limits_check #i.e. -np.inf

        objective = self.standard_objective_function(fit_process_parameters)

        return -objective

    def fit(self, initial_population=[], computational_pool=False):

        start_time = python_time.time()
        #Safety, recompute in case user changes boundaries after init
        self.priors = parameters_priors.default_parameters_priors(
            self.priors_parameters)

        if initial_population == []:

            best_solution = self.initial_guess()

            if best_solution is None:

                return None

            number_of_parameters = len(best_solution)
            nwalkers = self.MCMC_walkers * number_of_parameters

            # Initialize the population of MCMC
            eps = 10 ** -4
            floors = np.floor(np.round(best_solution))
            initial = best_solution - floors
            mask = initial == 0
            initial[mask] = eps

            deltas = initial * np.random.uniform(-eps, eps,
                                                 (nwalkers, number_of_parameters))
            population = best_solution + deltas

        else:

            population = initial_population[:, :-1]
            number_of_parameters = population.shape[1]

            nwalkers = self.MCMC_walkers * number_of_parameters

        nlinks = self.MCMC_links

        if computational_pool:

            pool = computational_pool

        else:
            pool = None

        try:
            # create a new MPI pool
            from schwimmbad import MPIPool
            pool = MPIPool()
            if not pool.is_master():
                pool.wait()
                sys.exit(0)
        except ModuleNotFoundError:

            pass

        if pool:

            with pool:

                sampler = emcee.EnsembleSampler(nwalkers, number_of_parameters,
                                                self.objective_function, pool=pool)

                sampler.run_mcmc(population, nlinks, progress=True)
        else:

            sampler = emcee.EnsembleSampler(nwalkers, number_of_parameters,
                                            self.objective_function, pool=pool)

            sampler.run_mcmc(population, nlinks, progress=True)

        computation_time = python_time.time() - start_time
        print(sys._getframe().f_code.co_name, ' : ' + self.fit_type() + ' fit SUCCESS')

        self.trials = np.array(self.trials)
        self.trials[:, -1] *= -1

        MCMC_chains, MCMC_chains_with_fluxes = self.reconstruct_chains(
            sampler.get_chain(), sampler.get_log_prob())

        best_model_index = np.where(
            MCMC_chains[:, :, -1] == MCMC_chains[:, :, -1].max())
        fit_results = MCMC_chains_with_fluxes[np.unique(best_model_index[0])[0],
                      np.unique(best_model_index[1])[0], :-1]
        fit_log_likelihood = MCMC_chains[
            np.unique(best_model_index[0])[0], np.unique(best_model_index[1])[0], -1]

        print('best_model:', fit_results, self.loss_function, fit_log_likelihood)

        self.fit_results = {'best_model': fit_results,
                            self.loss_function: fit_log_likelihood,
                            'MCMC_chains': MCMC_chains,
                            'MCMC_chains_with_fluxes': MCMC_chains_with_fluxes,
                            'fit_time': computation_time}

    def reconstruct_chains(self, mcmc_samples, mcmc_prob):

        rangei, rangej, rangek = mcmc_samples.shape

        if self.telescopes_fluxes_method == 'polyfit':
            Rangei,Rangej = self.trials.shape
            MCMC_chains_with_fluxes = np.zeros((rangei,rangej,Rangej))

            for j in range(rangej):

                    unique_sample = np.unique(mcmc_samples[:,j],return_inverse=True,
                                              axis=0)

                    unique_trials = []
                    for unique_values in unique_sample[0]:

                        index = np.where(self.trials[:,:len(self.fit_parameters)][:,-1]
                                         ==unique_values[-1])[0][0]
                        unique_trials.append(self.trials[index].tolist())
                    MCMC_chains_with_fluxes[:,j] = np.array(unique_trials)[unique_sample[1].ravel()]

            columns_to_swap = []
            if self.rescale_photometry:
                columns_to_swap += self.rescale_photometry_parameters_index

            if self.rescale_astrometry:
                columns_to_swap += self.rescale_photometry_parameters_index

            if (columns_to_swap != []):

                old_column = columns_to_swap
                new_column = np.arange(old_column[-1]+1,Rangej-1,1).tolist()

                MCMC_chains_with_fluxes[:, :, old_column + new_column] = MCMC_chains_with_fluxes[:, :,
                                                                     new_column + old_column]


        else:

            MCMC_chains_with_fluxes = mcmc_samples.copy()



        MCMC_chains = np.zeros((rangei, rangej, rangek + 1))
        MCMC_chains[:, :, :-1] = mcmc_samples
        MCMC_chains[:, :, -1] = mcmc_prob



        return MCMC_chains, MCMC_chains_with_fluxes

    def samples_to_plot(self):

        chains = self.fit_results['MCMC_chains_with_fluxes']
        samples = chains.reshape(-1, chains.shape[2])
        samples_to_plot = samples[int(len(samples) / 2):]

        return samples_to_plot
