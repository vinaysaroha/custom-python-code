import boto3

import xlsxwriter

instance_id = []

instance_name = []

instance_state = []

region = "ap-southeast-2"

client = boto3.client('ec2', region_name=region)

instance_detail = client.describe_instances()

count1 = 0

count2 = 0

count3 = 0

for instance in instance_detail['Reservations']:

    for printout in instance['Instances']:

        for printname in printout['Tags']:

         if printname['Key'] == 'Name':  

            print(printout['InstanceId'],'---->',printout["InstanceType"],"---->", printname["Value"],"---->" ,printout['State']['Name'])

            # instance_type = list(printout["InstanceType"])

            # if ((instance_type[0] == 't' and instance_type[1] == '2') or (instance_type[0] == 'm' and instance_type[1] == '4') or (instance_type[0] == 'c' and instance_type[1] == '4') or (instance_type[0] == 'r' and instance_type[1] == '4')) and ((printout['State']['Name'] == "running" or printout['State']['Name'] == "stopped")):

            #     print(printout['InstanceId'],'---->',printout["InstanceType"],"---->", printname["Value"],"---->" ,printout['State']['Name'])

            # instance_id.append(printout['InstanceId'])

            instance_name.append(printname["Value"])

            instance_state.append(printout['State']['Name'])

 

instance_ids_count = 1

instance_lables_count = 1

instance_states_count = 1

outWorkbook = xlsxwriter.Workbook("out.xlsx")

outSheet = outWorkbook.add_worksheet()

instance_ids = instance_id

instance_names = instance_name

instance_states = instance_state

outSheet.write("A1", "Instance_Id")

outSheet.write("B1", "Instance_Name")

outSheet.write("C1", "Instance_State")

for each_instance_id in instance_ids:

    outSheet.write(instance_ids_count, 0, instance_ids[count1])

    instance_ids_count+=1

    count1+=1

for each_instance_name in instance_names:

    outSheet.write(instance_lables_count, 1, instance_names[count2])

    instance_lables_count+=1

    count2+=1

for each_instance_state in instance_states:

    outSheet.write(instance_states_count, 2, instance_states[count3])

    instance_states_count+=1

    count3+=1
    
outWorkbook.close()