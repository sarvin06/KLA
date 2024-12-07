import json
from collections import defaultdict

# Load JSON data
data = {
  "steps": [
    {
      "id": "S1",
      "parameters": { "P1": [ 100, 200 ] },
      "dependency": None
    },
    {
      "id": "S2",
      "parameters": { "P1": [ 100, 200 ] },
      "dependency": None
    }
  ],
  "machines": [
    {
      "machine_id": "M1",
      "step_id": "S1",
      "cooldown_time": 5,
      "initial_parameters": { "P1": 100 },
      "fluctuation": { "P1": 5 },
      "n": 20
    },
    {
      "machine_id": "M2",
      "step_id": "S2",
      "cooldown_time": 5,
      "initial_parameters": { "P1": 100 },
      "fluctuation": { "P1": 5 },
      "n": 20
    },
    {
      "machine_id": "M3",
      "step_id": "S2",
      "cooldown_time": 5,
      "initial_parameters": { "P1": 100 },
      "fluctuation": { "P1": 5 },
      "n": 20
    }
  ],
  "wafers": [
    {
      "type": "W1",
      "processing_times": {
        "S1": 10,
        "S2": 15
      },
      "quantity": 3
    }
  ]
}

# Initialize schedule and tracking structures
schedule = []
machine_availability = defaultdict(lambda: 0)  # Tracks when each machine becomes available

# Assign wafers to steps and machines
wafer_count = 1
for wafer in data["wafers"]:
    for wafer_instance in range(wafer["quantity"]):
        wafer_id = f"{wafer['type']}-{wafer_count}"
        current_time = 0
        for step in data["steps"]:
            step_id = step["id"]
            processing_time = wafer["processing_times"][step_id]

            # Find a suitable machine for the step
            available_machines = [
                machine for machine in data["machines"] if machine["step_id"] == step_id
            ]
            available_machines.sort(key=lambda m: machine_availability[m["machine_id"]])
            selected_machine = available_machines[0]
            machine_id = selected_machine["machine_id"]

            # Schedule the wafer step
            start_time = max(current_time, machine_availability[machine_id])
            end_time = start_time + processing_time
            schedule.append({
                "wafer_id": wafer_id,
                "step": step_id,
                "machine": machine_id,
                "start_time": start_time,
                "end_time": end_time
            })

            # Update machine availability and current time
            machine_availability[machine_id] = end_time + selected_machine["cooldown_time"]
            current_time = end_time

        wafer_count += 1

# Print the generated schedule
print(json.dumps(schedule, indent=2))
