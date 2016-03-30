#import sys
#sys.path.append('.')
import learn as l
import math
import pickle as pk

obs1 = []
gamma = 1.0

def get_state(buffer_len, throughput):
    buf_len = float(buffer_len)
    buf_len = math.floor(buf_len)
    buf_len = int(buf_len)

    T = float(throughput)
    T = math.floor(T)
    T = int(T)
    if (T >= 100):
        T = 99

    return str(buf_len) + "," + str(T)
    #return [buf_len, T]
    #return buf_len * 100 + T

def get_action(next_quality):
    return int(next_quality)

def get_reword(next_quality, next_no_rebuffer, next_buflen) :
    next_no_rebuffer = int(next_no_rebuffer) #0:rebuffer
    next_buflen = float(next_buflen)
    next_quality = int(next_quality)

    r = float(next_no_rebuffer)
    q = float(next_quality)
    l = next_buflen

    if (next_no_rebuffer == 0) :
        return 0#float("-Inf")
    return 1
    R = q * l
    return R


def add_to_dict(now, next) :
    global obs1
    tnow = now.strip().split(' ')
    tnext = next.strip().split(' ')
    
    S = get_state(tnow[1], tnow[2])
    A = get_action(tnow[3])
    R = get_reword(tnow[3], tnext[0], tnext[1])

    obs1.append([S, A, R])

def get_obs():
    for i in range(1, 1001):
        fn = "../../logs/rand" + str(i) + ".log"
        fp = open(fn, "r")
        lines = fp.readlines()
        for j in range(len(lines)-1):
            add_to_dict(lines[j], lines[j + 1])
        fp.close()

if __name__ == "__main__":
    print "Collecting observations ..."
    get_obs()
    
    obs = [obs1]
    print "Learning ..."
    model = l.learn(obs, gamma, 5, True, 0.001)
    
    print "Storing model"
    fp = open("model.pk", "wb")
    pk.dump(model, fp)

    fp.close()
    print "Done!"




    
    
    
