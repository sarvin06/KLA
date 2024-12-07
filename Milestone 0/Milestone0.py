import json

# Load the JSON file
with open("D:\\Milestone 0\\Milestone0.json", "r") as file:
    data = json.load(file)

# Extracting relevant data
steps = data['steps']
machines = data['machines']
wafers = data['wafers']

# Initialize variables
wafer_count = wafers[0]["quantity"]
process_time = wafers[0]["processing_times"]

# Availability and scheduling
is_machine_available = [True] * len(machines)
processed_steps = [[False] * len(process_time) for _ in range(wafer_count)]
schedule = []

# Scheduling logic
for i in range(wafer_count):
    wafer_id = f"W1-{i+1}"
    start_time = 0
    for j, step in enumerate(process_time):
        for m_idx, machine in enumerate(machines):
            if machine["step_id"] == step and is_machine_available[m_idx] and not processed_steps[i][j]:
                is_machine_available[m_idx] = False

                # Calculate start and end times
                end_time = start_time + process_time[step]
                schedule.append({
                    "wafer_id": wafer_id,
                    "step": step,
                    "machine": machine["machine_id"],
                    "start_time": start_time,
                    "end_time": end_time,
                })

                # Update tracking variables
                start_time = end_time
                processed_steps[i][j] = True
                is_machine_available[m_idx] = True
                break

# Output the schedule
print(json.dumps({"schedule": schedule}, indent=4))
