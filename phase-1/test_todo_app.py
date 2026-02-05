"""
Simple test to verify Todo Console App functionality.
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.todo import TodoList, Task

def test_todo_functionality():
    """Test the core functionality of the TodoList."""
    print("Testing Todo Console App functionality...")

    # Create a new todo list
    todo_list = TodoList()

    # Test 1: Add a task
    print("\n1. Testing add task functionality...")
    task1 = todo_list.add_task("Buy groceries")
    print(f"   Added task: {task1}")
    assert task1.description == "Buy groceries"
    assert task1.completed == False
    assert task1.id == 1
    print("   [PASS] Task added successfully")

    # Test 2: Add another task
    task2 = todo_list.add_task("Walk the dog")
    print(f"   Added task: {task2}")
    assert task2.id == 2
    print("   [PASS] Second task added successfully")

    # Test 3: Get all tasks
    print("\n2. Testing get all tasks...")
    all_tasks = todo_list.get_all_tasks()
    assert len(all_tasks) == 2
    print(f"   Retrieved {len(all_tasks)} tasks")
    print("   [PASS] All tasks retrieved successfully")

    # Test 4: Get specific task
    print("\n3. Testing get specific task...")
    retrieved_task = todo_list.get_task(1)
    assert retrieved_task is not None
    assert retrieved_task.description == "Buy groceries"
    print(f"   Retrieved task ID 1: {retrieved_task}")
    print("   [PASS] Specific task retrieved successfully")

    # Test 5: Update task
    print("\n4. Testing update task...")
    update_success = todo_list.update_task(1, "Buy groceries and cook dinner")
    assert update_success == True
    updated_task = todo_list.get_task(1)
    assert updated_task.description == "Buy groceries and cook dinner"
    print(f"   Updated task: {updated_task}")
    print("   [PASS] Task updated successfully")

    # Test 6: Toggle task status
    print("\n5. Testing toggle task status...")
    initial_status = task1.completed
    toggle_success = todo_list.toggle_task_status(1)
    assert toggle_success == True
    toggled_task = todo_list.get_task(1)
    assert toggled_task.completed != initial_status
    print(f"   Toggled task status: {toggled_task}")
    print("   [PASS] Task status toggled successfully")

    # Test 7: Delete task
    print("\n6. Testing delete task...")
    delete_success = todo_list.delete_task(2)
    assert delete_success == True
    remaining_tasks = todo_list.get_all_tasks()
    assert len(remaining_tasks) == 1
    print(f"   Remaining tasks after deletion: {len(remaining_tasks)}")
    print("   [PASS] Task deleted successfully")

    # Test 8: Try to get deleted task (should return None)
    print("\n7. Testing retrieval of deleted task...")
    deleted_task = todo_list.get_task(2)
    assert deleted_task is None
    print("   [PASS] Deleted task correctly returns None")

    # Test 9: Test error handling for empty description
    print("\n8. Testing error handling for empty description...")
    try:
        todo_list.add_task("")
        assert False, "Should have raised ValueError"
    except ValueError:
        print("   [PASS] Empty description correctly raises ValueError")

    print("\n[PASS] All tests passed! Todo Console App functionality is working correctly.")

if __name__ == "__main__":
    test_todo_functionality()