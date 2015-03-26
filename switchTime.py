#! /usr/bin/env python

# Calculate context switch duration

log = open('log','r')
lines = log.readlines()
costTime = open('switchLog','w')


context_switch = []

for line in lines :
    line = line.strip()
    inst, args = line.split(' ' , 1)

    if inst == 'switch' : 
        out_task, in_task, tick, tick_reload, out_minitick, in_minitick = args.split(' ')
        out_time = (float(tick) + (float(tick_reload) - float(out_minitick)) / float(tick_reload)) /100 * 1000;
        in_time  = (float(tick) + (float(tick_reload) - float(in_minitick))  / float(tick_reload)) /100 * 1000;

        information = {}
        information['out'] = out_task
        information['in'] = in_task
        information['duration'] = in_time - out_time
        costTime.write('switch from %s to %s costs %f seconds\n' % (information['out'], information['in'], information['duration']) )
 #       context_switch.append(information)

log.close()

#for information in context_switch : 
#    costTime.write('switch from %s to %s costs %f seconds\n' % (information['out'], information['in'], information['duration']) )

costTime.close()






