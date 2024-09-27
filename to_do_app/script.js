document.getElementById('add-task-btn').addEventListener('click', function() {
    let taskText = document.getElementById('new-task').value;

    if (taskText === '') {
        alert('Please enter a task.');
        return;
    }

    let taskList = document.getElementById('task-list');
    let listItem = document.createElement('li');
    listItem.textContent = taskText;

    let deleteBtn = document.createElement('button');
    deleteBtn.textContent = 'Delete';
    deleteBtn.addEventListener('click', function() {
        taskList.removeChild(listItem);
    });

    listItem.appendChild(deleteBtn);
    taskList.appendChild(listItem);

    document.getElementById('new-task').value = '';
});
