import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import upload_file  # Import the upload_file function


# Call the upload_file function to obtain sample_rate and data
sample_rate, data = wavfile.read(upload_file.upload_file())
# Compute the spectrogram of the audio data
spectrum, freqs, t, im = plt.specgram(data, Fs=sample_rate, NFFT=1024, cmap=plt.get_cmap('autumn_r'))
plt.title('Spectrogram')  # Plotting the Spectrogram first


#HIGH
# Function to find the target frequency
def find_high_target_frequency(freqs):
    for x in freqs:
        if x > 5000:
            break
    return x


#MID
# Function to find the target frequency
def find_mid_target_frequency(freqs):
    for x in freqs:
        if x > 1000:
            break
    return x


#LOW
# Function to find the target frequency
def find_low_target_frequency(freqs):
    for x in freqs:
        if x > 100:
            break
    return x


def frequency_low_check():
    target_frequency = find_low_target_frequency(freqs)
    index_of_frequency = np.where(freqs == target_frequency)[0][0]

    # Get the data for the particular frequency
    data_for_frequency = spectrum[index_of_frequency]

    # Handle zeros or very small values in data_for_frequency to avoid divide by zero
    epsilon = 1e-9  # Small value to avoid log(0)
    data_for_frequency = np.maximum(data_for_frequency, epsilon)

    # Convert the digital signal to values in decibels
    data_in_db_fun = 10 * np.log10(data_for_frequency)
    return data_in_db_fun


def frequency_mid_check():
    target_frequency = find_mid_target_frequency(freqs)
    index_of_frequency = np.where(freqs == target_frequency)[0][0]

    # Get the data for the particular frequency
    data_for_frequency = spectrum[index_of_frequency]

    # Handle zeros or very small values in data_for_frequency to avoid divide by zero
    epsilon = 1e-9  # Small value to avoid log(0)
    data_for_frequency = np.maximum(data_for_frequency, epsilon)

    # Convert the digital signal to values in decibels
    data_in_db_fun = 10 * np.log10(data_for_frequency)
    return data_in_db_fun


# Function to perform frequency check and conversion to decibels
def frequency_high_check():
    target_frequency = find_high_target_frequency(freqs)
    index_of_frequency = np.where(freqs == target_frequency)[0][0]

    # Get the data for the particular frequency
    data_for_frequency = spectrum[index_of_frequency]

    # Handle zeros or very small values in data_for_frequency to avoid divide by zero
    epsilon = 1e-9  # Small value to avoid log(0)
    data_for_frequency = np.maximum(data_for_frequency, epsilon)

    # Convert the digital signal to values in decibels
    data_in_db_fun = 10 * np.log10(data_for_frequency)
    return data_in_db_fun


# Function to find the nearest value in an array
def find_nearest_value(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]


# Call frequency_check to obtain data in decibels
mid_data_in_db = frequency_mid_check()
low_data_in_db = frequency_low_check()
high_data_in_db = frequency_high_check()


## HIGH FREQUENCY CALCULATONS
# Find the index of the maximum value
index_of_high_max = np.argmax(high_data_in_db)
value_of_high_max = high_data_in_db[index_of_high_max]
# Slice the array from the maximum value
sliced_high_array = high_data_in_db[index_of_high_max:]
# Find the nearest value to max - 5 dB
value_of_high_max_less_5 = value_of_high_max - 5
value_of_high_max_less_5 = find_nearest_value(sliced_high_array, value_of_high_max_less_5)
index_of_high_max_less_5 = np.where(high_data_in_db == value_of_high_max_less_5)[0][0]
# Find the nearest value to max - 25 dB
value_of_high_max_less_25 = value_of_high_max - 25
value_of_high_max_less_25 = find_nearest_value(sliced_high_array, value_of_high_max_less_25)
index_of_high_max_less_25 = np.where(high_data_in_db == value_of_high_max_less_25)[0][0]


## MID FREQUENCY CALCULATONS
# Find the index of the maximum value
index_of_mid_max = np.argmax(mid_data_in_db)
value_of_mid_max = mid_data_in_db[index_of_mid_max]
# Slice the array from the maximum value
sliced_mid_array = mid_data_in_db[index_of_mid_max:]
# Find the nearest value to max - 5 dB
value_of_mid_max_less_5 = value_of_mid_max - 5
value_of_mid_max_less_5 = find_nearest_value(sliced_mid_array, value_of_mid_max_less_5)
index_of_mid_max_less_5 = np.where(mid_data_in_db == value_of_mid_max_less_5)[0][0]
# Find the nearest value to max - 25 dB
value_of_mid_max_less_25 = value_of_mid_max - 25
value_of_mid_max_less_25 = find_nearest_value(sliced_mid_array, value_of_mid_max_less_25)
index_of_mid_max_less_25 = np.where(mid_data_in_db == value_of_mid_max_less_25)[0][0]

## LOW FREQUENCY CALCULATONS
# Find the index of the maximum value
index_of_low_max = np.argmax(low_data_in_db)
value_of_low_max = low_data_in_db[index_of_low_max]
# Slice the array from the maximum value
sliced_low_array = low_data_in_db[index_of_low_max:]
# Find the nearest value to max - 5 dB
value_of_low_max_less_5 = value_of_low_max - 5
value_of_low_max_less_5 = find_nearest_value(sliced_low_array, value_of_low_max_less_5)
index_of_low_max_less_5 = np.where(low_data_in_db == value_of_low_max_less_5)[0][0]
# Find the nearest value to max - 25 dB
value_of_low_max_less_25 = value_of_low_max - 25
value_of_low_max_less_25 = find_nearest_value(sliced_low_array, value_of_low_max_less_25)
index_of_low_max_less_25 = np.where(low_data_in_db == value_of_low_max_less_25)[0][0]


# Plot each line graph in a separate window


def plot_waveform():
    # Plot 1: Waveform
    wave_plot = plt.figure()
    plt.plot(data)
    plt.title('Waveform')
    return wave_plot


# Plot 2: Combined RT60 Line Graph (with data points)
def plot_rt60_lmh_data():
    lmh_data_plot = plt.figure()
    # Plot lines of low, mid, and high data on graph
    plt.plot(t, high_data_in_db, color="#84FF94")
    plt.plot(t, mid_data_in_db, color="#FFDD84")
    plt.plot(t, low_data_in_db, color="#FF8484")

    # Plot index values for high frequencies
    plt.scatter(t[index_of_high_max], high_data_in_db[index_of_high_max],
                color='#00FF21', label=f'Max: {t[index_of_high_max]:.2f} dB')
    plt.scatter(t[index_of_high_max_less_5], high_data_in_db[index_of_high_max_less_5],
                color='#00A916', label=f'Max: {value_of_high_max_less_5:.2f} dB')
    plt.scatter(t[index_of_high_max_less_25], high_data_in_db[index_of_high_max_less_25],
                color='#00750F', label=f'Max: {value_of_high_max_less_25:.2f} dB')

    # Plot index values for mid frequencies
    plt.scatter(t[index_of_mid_max], mid_data_in_db[index_of_mid_max],
                color='#FFB900', label=f'Max: {t[index_of_mid_max]:.2f} dB')
    plt.scatter(t[index_of_mid_max_less_5], mid_data_in_db[index_of_mid_max_less_5],
                color='#AA7C00', label=f'Max: {value_of_mid_max_less_5:.2f} dB')
    plt.scatter(t[index_of_mid_max_less_25], mid_data_in_db[index_of_mid_max_less_25],
                color='#815E00', label=f'Max: {value_of_mid_max_less_25:.2f} dB')

    # Plot index values for low frequencies
    plt.scatter(t[index_of_low_max], low_data_in_db[index_of_low_max],
                color='#FF0000', label=f'Max: {t[index_of_low_max]:.2f} dB')
    plt.scatter(t[index_of_low_max_less_5], low_data_in_db[index_of_low_max_less_5],
                color='#A00000', label=f'Max: {value_of_low_max_less_5:.2f} dB')
    plt.scatter(t[index_of_low_max_less_25], low_data_in_db[index_of_low_max_less_25],
                color='#800000', label=f'Max: {value_of_low_max_less_25:.2f} dB')
    plt.title('RT60: Lo, Mi, Hi')
    plt.legend()
    return lmh_data_plot


def plot_rt60_lmh():
    lmh_plot = plt.figure()
    # Plot lines of low, mid, and high data on graph
    plt.plot(t, high_data_in_db, color="#84FF94")
    plt.plot(t, mid_data_in_db, color="#FFDD84")
    plt.plot(t, low_data_in_db, color="#FF8484")
    # plot time index values for high frequencies
    plt.scatter(t[index_of_high_max], high_data_in_db[index_of_high_max], color='#00FF21')
    plt.scatter(t[index_of_high_max_less_5], high_data_in_db[index_of_high_max_less_5], color='#00A916')
    plt.scatter(t[index_of_high_max_less_25], high_data_in_db[index_of_high_max_less_25], color='#00750F')
    # plot time index values for mid frequencies
    plt.scatter(t[index_of_mid_max], mid_data_in_db[index_of_mid_max], color='#FFB900')
    plt.scatter(t[index_of_mid_max_less_5], mid_data_in_db[index_of_mid_max_less_5], color='#AA7C00')
    plt.scatter(t[index_of_mid_max_less_25], mid_data_in_db[index_of_mid_max_less_25], color='#815E00')
    # plot time index values for low frequencies
    plt.scatter(t[index_of_low_max], low_data_in_db[index_of_low_max], color='#FF0000')
    plt.scatter(t[index_of_low_max_less_5], low_data_in_db[index_of_low_max_less_5], color='#A00000')
    plt.scatter(t[index_of_low_max_less_25], low_data_in_db[index_of_low_max_less_25], color='#800000')
    plt.title('RT60: Low, Mid, High')
    plt.legend()
    return lmh_plot


def plot_rt60_high_data():
    high_data_plot = plt.figure()
    plt.plot(t, high_data_in_db, color="#84FF94")
    # plot time index values for high frequencies
    plt.scatter(t[index_of_high_max], high_data_in_db[index_of_high_max],
                color='#00FF21', label=f'Max: {t[index_of_high_max]:.2f} dB')
    plt.scatter(t[index_of_high_max_less_5], high_data_in_db[index_of_high_max_less_5],
                color='#00A916', label=f'Max: {value_of_high_max_less_5:.2f} dB')
    plt.scatter(t[index_of_high_max_less_25], high_data_in_db[index_of_high_max_less_25],
                color='#00750F', label=f'Max: {value_of_high_max_less_25:.2f} dB')
    plt.title('RT60: High')
    plt.legend()
    return high_data_plot


def plot_rt60_high():
    high_plot = plt.figure()
    plt.plot(t, high_data_in_db, color="#84FF94")
    # plot time index values for high frequencies
    plt.scatter(t[index_of_high_max], high_data_in_db[index_of_high_max], color='#00FF21')
    plt.scatter(t[index_of_high_max_less_5], high_data_in_db[index_of_high_max_less_5], color='#00A916')
    plt.scatter(t[index_of_high_max_less_25], high_data_in_db[index_of_high_max_less_25], color='#00750F')
    plt.title('RT60: High')
    plt.legend()
    return high_plot


def plot_rt60_mid_data():
    mid_data_plot = plt.figure()
    plt.plot(t, mid_data_in_db, color="#FFDD84")
    # plot time index values for mid frequencies
    plt.scatter(t[index_of_mid_max], mid_data_in_db[index_of_mid_max],
                color='#FFB900', label=f'Max: {t[index_of_mid_max]:.2f} dB')
    plt.scatter(t[index_of_mid_max_less_5], mid_data_in_db[index_of_mid_max_less_5],
                color='#AA7C00', label=f'Max: {value_of_mid_max_less_5:.2f} dB')
    plt.scatter(t[index_of_mid_max_less_25], mid_data_in_db[index_of_mid_max_less_25],
                color='#815E00', label=f'Max: {value_of_mid_max_less_25:.2f} dB')
    plt.title('RT60: Mid')
    plt.legend()
    return mid_data_plot


def plot_rt60_mid():
    mid_plot = plt.figure()
    plt.plot(t, mid_data_in_db, color="#FFDD84")
    # plot time index values for mid frequencies
    plt.scatter(t[index_of_mid_max], mid_data_in_db[index_of_mid_max], color='#FFB900')
    plt.scatter(t[index_of_mid_max_less_5], mid_data_in_db[index_of_mid_max_less_5], color='#AA7C00')
    plt.scatter(t[index_of_mid_max_less_25], mid_data_in_db[index_of_mid_max_less_25], color='#815E00')
    plt.title('RT60: Mid')
    plt.legend()
    return mid_plot


def plot_rt60_low_data():
    low_data_plot = plt.figure()
    plt.plot(t, low_data_in_db, color="#FF8484")
    # plot time index values for low frequencies
    plt.scatter(t[index_of_low_max], low_data_in_db[index_of_low_max],
                color='#FF0000', label=f'Max: {t[index_of_low_max]:.2f} dB')
    plt.scatter(t[index_of_low_max_less_5], low_data_in_db[index_of_low_max_less_5],
                color='#A00000', label=f'Max: {value_of_low_max_less_5:.2f} dB')
    plt.scatter(t[index_of_low_max_less_25], low_data_in_db[index_of_low_max_less_25],
                color='#800000', label=f'Max: {value_of_low_max_less_25:.2f} dB')
    plt.title('RT60: Low')
    plt.legend()
    return low_data_plot


def plot_rt60_low():
    low_plot = plt.figure()
    plt.plot(t, low_data_in_db, color="#FF8484")
    # plot time index values for low frequencies
    plt.scatter(t[index_of_low_max], low_data_in_db[index_of_low_max], color='#FF0000')
    plt.scatter(t[index_of_low_max_less_5], low_data_in_db[index_of_low_max_less_5], color='#A00000')
    plt.scatter(t[index_of_low_max_less_25], low_data_in_db[index_of_low_max_less_25], color='#800000')
    plt.title('RT60: Low')
    plt.legend()
    return low_plot


def rt60_high():
    # Calculate RT20 and extrapolate to RT60 for mid freq
    rt20 = t[index_of_high_max_less_5] - t[index_of_high_max_less_25]
    rt60 = 3 * rt20
    return round(abs(rt60), 2)


def rt60_mid():
    # Calculate RT20 and extrapolate to RT60 for mid freq
    rt20 = t[index_of_mid_max_less_5] - t[index_of_mid_max_less_25]
    rt60 = 3 * rt20
    return round(abs(rt60), 2)


def rt60_low():
    # Calculate RT20 and extrapolate to RT60 for mid freq
    rt20 = t[index_of_low_max_less_5] - t[index_of_low_max_less_25]
    rt60 = 3 * rt20
    return round(abs(rt60), 2)


# Display all open plot windows
plot_waveform()
plot_rt60_lmh_data()
plot_rt60_lmh()
plot_rt60_high_data()
plot_rt60_high()
plot_rt60_mid_data()
plot_rt60_mid()
plot_rt60_low_data()
plot_rt60_low()
plt.show()
