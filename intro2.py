import numpy as np  # Module that simplifies computations on matrices
import matplotlib.pyplot as plt  # Module used for plotting
from pylsl import StreamInlet, resolve_byprop  # Module to receive EEG data
import time

BUFFER_LENGTH = 5

# Length of the epochs used to compute the FFT (in seconds)
EPOCH_LENGTH = 1

# Amount of overlap between two consecutive epochs (in seconds)
OVERLAP_LENGTH = 0.8

# Amount to 'shift' the start of each next consecutive epoch
SHIFT_LENGTH = EPOCH_LENGTH - OVERLAP_LENGTH

if __name__ == "__main__":

 print('Looking for an EEG stream...')
 streams = resolve_byprop('type', 'EEG', timeout=2)
 print(streams)
 if len(streams) == 0:
  raise RuntimeError('Can\'t find EEG stream.')
 print("Start acquiring data")
 inlet = StreamInlet(streams[0], max_chunklen=12)
 print(inlet)
 eeg_time_correction = inlet.time_correction()
 print(eeg_time_correction)
 info = inlet.info()
 print(info)
 description = info.desc()
 print(description)
 fs = int(info.nominal_srate())
 print(fs)

 itr=0
 
 print(time.time())
 try:
        
  while itr<10:
   eeg_data, timestamp = inlet.pull_chunk(timeout=1, max_samples=int(SHIFT_LENGTH * fs))
   print(eeg_data)     
   print('\n')
   #ch_data = np.array(eeg_data)[:, INDEX_CHANNEL]
   itr=itr+1
   print(itr) 
   print('\n')
   print(time.time())
   print('\n')

 except KeyboardInterrupt:
  print('Closing!')
  
  