from ydata_synthetic.preprocessing.regular.adult import transformations
from ydata_synthetic.synthesizers.regular import WGAN_GP
from ydata_synthetic.synthesizers import ModelParameters, TrainParameters

#Load and process the data
data, processed_data, preprocessor = transformations()

# WGAN_GP training
#Defining the training parameters of WGAN_GP

noise_dim = 32
dim = 128
batch_size = 128

log_step = 100
epochs = 300+1
learning_rate = [5e-4, 3e-3]
beta_1 = 0.5
beta_2 = 0.9
models_dir = './cache'

gan_args = ModelParameters(batch_size=batch_size,
                           lr=learning_rate,
                           betas=(beta_1, beta_2),
                           noise_dim=noise_dim,
                           n_cols=processed_data.shape[1],
                           layers_dim=dim)

train_args = TrainParameters(epochs=epochs,
                             sample_interval=log_step)

synthesizer = WGAN_GP(gan_args, n_critic=2)
synthesizer.train(processed_data, train_args)

synth_data = synthesizer.sample(1000)
synthesizer.save('test.pkl')
