'use client';

import { useState, useEffect } from 'react';
import { Task } from '@/types/task';

export default function Home() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [newTask, setNewTask] = useState({ title: '', description: '' });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // In a real app, you would get the user ID from authentication context
  const userId = 'user123'; // Placeholder - in real app this would come from auth

  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {
    try {
      setLoading(true);
      // Placeholder API call - in real app this would call your backend
      // const response = await fetch(`/api/${userId}/tasks`);
      // const data = await response.json();
      // setTasks(data);

      // Mock data for demonstration
      setTasks([
        { id: 1, title: 'Sample Task', description: 'This is a sample task', completed: false, user_id: userId, created_at: new Date().toISOString(), updated_at: new Date().toISOString() },
        { id: 2, title: 'Another Task', description: 'This is another sample task', completed: true, user_id: userId, created_at: new Date().toISOString(), updated_at: new Date().toISOString() }
      ]);
    } catch (err) {
      setError('Failed to fetch tasks');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleAddTask = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!newTask.title.trim()) return;

    try {
      // Placeholder API call - in real app this would call your backend
      // const response = await fetch(`/api/${userId}/tasks`, {
      //   method: 'POST',
      //   headers: { 'Content-Type': 'application/json' },
      //   body: JSON.stringify(newTask)
      // });
      // const createdTask = await response.json();

      // Mock creation for demonstration
      const createdTask: Task = {
        id: tasks.length + 1,
        title: newTask.title,
        description: newTask.description,
        completed: false,
        user_id: userId,
        created_at: new Date().toISOString(),
        updated_at: new Date().toISOString()
      };

      setTasks([...tasks, createdTask]);
      setNewTask({ title: '', description: '' });
    } catch (err) {
      setError('Failed to add task');
      console.error(err);
    }
  };

  const toggleTaskCompletion = async (id: number) => {
    try {
      // Placeholder API call - in real app this would call your backend
      // const response = await fetch(`/api/${userId}/tasks/${id}/complete`, {
      //   method: 'PATCH'
      // });
      // const updatedTask = await response.json();

      // Mock update for demonstration
      setTasks(tasks.map(task =>
        task.id === id ? { ...task, completed: !task.completed } : task
      ));
    } catch (err) {
      setError('Failed to update task');
      console.error(err);
    }
  };

  const deleteTask = async (id: number) => {
    try {
      // Placeholder API call - in real app this would call your backend
      // await fetch(`/api/${userId}/tasks/${id}`, { method: 'DELETE' });

      // Mock deletion for demonstration
      setTasks(tasks.filter(task => task.id !== id));
    } catch (err) {
      setError('Failed to delete task');
      console.error(err);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-white shadow">
        <div className="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
          <h1 className="text-3xl font-bold text-gray-900">Todo App</h1>
        </div>
      </header>
      <main>
        <div className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
          <div className="px-4 py-6 sm:px-0">
            <div className="bg-white shadow rounded-lg p-6">
              <h2 className="text-xl font-semibold mb-4">Add New Task</h2>
              <form onSubmit={handleAddTask} className="mb-6">
                <div className="mb-4">
                  <input
                    type="text"
                    value={newTask.title}
                    onChange={(e) => setNewTask({...newTask, title: e.target.value})}
                    placeholder="Task title"
                    className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
                    required
                  />
                </div>
                <div className="mb-4">
                  <textarea
                    value={newTask.description}
                    onChange={(e) => setNewTask({...newTask, description: e.target.value})}
                    placeholder="Task description (optional)"
                    className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
                    rows={3}
                  />
                </div>
                <button
                  type="submit"
                  className="w-full bg-indigo-600 text-white py-2 px-4 rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                >
                  Add Task
                </button>
              </form>

              {error && (
                <div className="mb-4 p-3 bg-red-100 text-red-700 rounded-md">
                  {error}
                </div>
              )}

              <h2 className="text-xl font-semibold mb-4">Your Tasks</h2>
              {loading ? (
                <p>Loading tasks...</p>
              ) : tasks.length === 0 ? (
                <p>No tasks found. Add a new task above!</p>
              ) : (
                <ul className="space-y-3">
                  {tasks.map((task) => (
                    <li
                      key={task.id}
                      className={`flex items-center justify-between p-3 border rounded-md ${task.completed ? 'bg-green-50' : 'bg-white'}`}
                    >
                      <div className="flex items-center">
                        <input
                          type="checkbox"
                          checked={task.completed}
                          onChange={() => toggleTaskCompletion(task.id)}
                          className="h-4 w-4 text-indigo-600 rounded focus:ring-indigo-500"
                        />
                        <span className={`ml-3 ${task.completed ? 'line-through text-gray-500' : 'text-gray-900'}`}>
                          <strong>{task.title}</strong>
                          {task.description && <div className="text-sm text-gray-500">{task.description}</div>}
                        </span>
                      </div>
                      <button
                        onClick={() => deleteTask(task.id)}
                        className="text-red-600 hover:text-red-900"
                      >
                        Delete
                      </button>
                    </li>
                  ))}
                </ul>
              )}
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}