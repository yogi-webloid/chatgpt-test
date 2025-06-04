import argparse
import json
from pathlib import Path

DATA_FILE = Path('tasks.json')
POINTS_FILE = Path('points.json')


def load_tasks():
    if DATA_FILE.exists():
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def load_points():
    if POINTS_FILE.exists():
        with open(POINTS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f).get('points', 0)
    return 0


def save_points(points):
    with open(POINTS_FILE, 'w', encoding='utf-8') as f:
        json.dump({'points': points}, f, ensure_ascii=False, indent=2)


def add_task(name, points):
    tasks = load_tasks()
    tasks.append({'name': name, 'points': points, 'done': False})
    save_tasks(tasks)
    print(f"Added task '{name}' worth {points} points")


def list_tasks():
    tasks = load_tasks()
    for idx, t in enumerate(tasks, start=1):
        status = '✓' if t.get('done') else '✗'
        print(f"{idx}. [{status}] {t['name']} ({t['points']} pts)")


def mark_done(task_id):
    tasks = load_tasks()
    if not (1 <= task_id <= len(tasks)):
        print('Invalid task ID')
        return
    task = tasks[task_id - 1]
    if task.get('done'):
        print('Task already completed')
        return
    task['done'] = True
    save_tasks(tasks)
    points = load_points() + task['points']
    save_points(points)
    print(f"Completed '{task['name']}'! Total points: {points}")


def show_status():
    points = load_points()
    print(f"Total points: {points}")


def parse_args():
    p = argparse.ArgumentParser(description='Gamified Task Manager')
    sub = p.add_subparsers(dest='command')

    add_p = sub.add_parser('add', help='Add a new task')
    add_p.add_argument('name', help='Task name')
    add_p.add_argument('--points', type=int, default=10, help='Points for the task')

    list_p = sub.add_parser('list', help='List all tasks')

    done_p = sub.add_parser('done', help='Mark task as done')
    done_p.add_argument('id', type=int, help='Task ID')

    sub.add_parser('status', help='Show total points')

    return p.parse_args()


def main():
    args = parse_args()
    if args.command == 'add':
        add_task(args.name, args.points)
    elif args.command == 'list':
        list_tasks()
    elif args.command == 'done':
        mark_done(args.id)
    elif args.command == 'status':
        show_status()
    else:
        print('No command provided. Use -h for help.')


if __name__ == '__main__':
    main()
