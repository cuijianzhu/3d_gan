import pickle
a = '/mnt/disk1/dat/lchen63/lrw/data/pickle/new_video_16_test.pkl'

train_data = pickle.load(a)
count = 0
total = len(train_data)
for inx in range(len(train_data)):
	for i in  range(0,16):
		lms_path = self.train_data[index][1 + i*3]
		melFrames = np.transpose(np.load(lms_path))
            if np.any(np.isinf(melFrames) ):
                count += 1 
                print "{}/{}".format(count,total)
                break