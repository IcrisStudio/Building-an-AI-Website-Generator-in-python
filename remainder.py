import time
from plyer import notification

def get_user_detail():
    tasks =[]
    task_count = int(input("enter the number of task: "))

   
    for i in range(task_count):
        task = input(f"enter the task {i + 1}: ")
        task_time = input(f"Enter the task time for {i + 1} (in format hour:minute): ")
        tasks.append((task, task_time))
    return tasks

def convert_into_seconds(time_str):
    hour, minute = map(int, time_str.split(":"))
    return hour * 3600 + minute * 60


def main():
    tasks = get_user_detail()

    while True:
        current_time = time.strftime("%I:%M", time.localtime())
        for task, task_time in tasks:
            if current_time == task_time:
                notification.notify(
                    title="Task Remainder",
                    message=f"It's time for {task}!",
                    timeout=20
                )
                tasks.remove((task, task_time))
        time.sleep(1)

if __name__ == "__main__":
    main()