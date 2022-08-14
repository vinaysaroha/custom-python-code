import boto3

import sys

from datetime import datetime, timedelta, timezone

 

 

def delete_ebs_volume(no_days):

    ec2_object = boto3.resource(service_name="ec2",region_name="ap-southeast-2")

    all_required_volume_id=[]

   

 

    print(datetime.now().date()-timedelta(days=no_days))

   

 

    for each_volume in ec2_object.volumes.all():

        if each_volume.state.lower() == "available":

            delete_time = (datetime.now().date() - timedelta(days=no_days))

            avd_clnp = False

            if each_volume.tags:

                for tag in each_volume.tags:

                    if (tag['Key'] == "AvoidCleanup"):

                        name = tag.get('Value')

                        if (name.lower() == 'true'):

                            avd_clnp = True

                            break

                   

            if (each_volume.create_time.date() < delete_time) and not avd_clnp:

                if each_volume.id not in all_required_volume_id:

                    all_required_volume_id.append(each_volume.id)

                    print(each_volume.id,"   ==    ", each_volume.state, "    ==    ",each_volume.create_time)

 

 

    print(f"count of available ebs not in use from last {no_days} days: {len(all_required_volume_id)}")

    for each_vol in all_required_volume_id:

        volume_ob = ec2_object.Volume(each_vol)

    print ("Deleting volume id" ,each_vol)

    volume_ob.delete 

    

        

if __name__ == "__main__":

    print(sys.argv)

    if len(sys.argv) >= 1:

        no_days = int(sys.argv[1])

        delete_ebs_volume(no_days)