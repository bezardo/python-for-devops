# Server configurations dictionary
server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}

# Retrieving information
def get_server_status(server_name):
    return server_config.get(server_name, {}).get('status', 'Server not found')

# Example usage
server_name = 'server2'
status = get_server_status(server_name)
print(f"{server_name} status: {status}")


###
instances_response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
active_instance_ids = set()

for reservation in instances_response['Reservations']:  
    for instance in reservation['Instances']:  
        active_instance_ids.add(instance['InstanceId'])
------
AWS Response Data (Simplified)
{
  "Reservations": [
    {
      "Instances": [
        {"InstanceId": "i-1111"},
        {"InstanceId": "i-2222"}
      ]
    },
    {
      "Instances": [
        {"InstanceId": "i-3333"},
        {"InstanceId": "i-1111"}  # Duplicate instance
      ]
    }
  ]
}
