import json

with open("D:\\Milestone 0\\Milestone0.json","r") as file:
    data=json.load(file)

# print(data)
# print(type(data))
# for i in data['steps']:
#     print(i,end='\n')
# for i in data['machines']:
#     print(i,end='\n')
# for i in data['wafers']:
#     print(i,end='\n')
steps=data['steps']
machines=data['machines']
wafers=data['wafers']



Total_time=0
#PROCESSING COUNT
count=wafers[0]["quantity"]
start_time=[0]*count
end_time=[0]*count
# print(steps,machines,wafers,sep='\n')


#Processing times
process_time=wafers[0]["processing_times"]
# print(process_time)


# p1up=[i for i in steps[]['parameters']]
p1up=[]
p1low=[]
for i in steps:
    p1up.append(i['parameters']['P1'][0])
    p1low.append(i['parameters']['P1'][1])

is_avail_machines=[True]*len(machines)
processed_steps=[]
for i in range(count):
    col=[]
    for j in range(len(process_time)):
        col.append(False)
    processed_steps.append(col)
setMaxTime=[0]*count

for i in range(0,count):
    wafer_id="w1-"+str(i+1)
    for j in range(len(process_time)):

        if is_avail_machines[j]==True and (not processed_steps[i][j]):
            is_avail_machines[j]=False
            print(processed_steps)

            processed_steps[i][j]=True
            step=machines[j]['step_id']
            machine=machines[j]['machine_id']
            start_time[i]=end_time[i]
            end_time[i]+=wafers[0]['processing_times'][step]
            setMaxTime[j]=wafers[0]['processing_times'][step]
   
            is_avail_machines[j]=True
            print(is_avail_machines)
            print(processed_steps[i][j])
            print(processed_steps)
            # for k in range(count):
            #     if start_time[j]>=setMaxTime[j]:
            #         is_avail_machines[j]=True

            print("wafer_id :",wafer_id,"step : ",step,"machine : ",machine,"start_time : ",start_time[i],"end_time : ",end_time[i])
    # for key,value in process_time:
    #     print(key,value)
