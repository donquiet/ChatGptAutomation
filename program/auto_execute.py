import os

# 생성할 파일의 경로와 내용 정의
files_content = {
    "to_do_app/my_first_page.html": '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>To-Do List</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>My To-Do List</h1>
        <input type="text" id="new-task" placeholder="Enter a new task">
        <button id="add-task-btn">Add Task</button>

        <ul id="task-list">
            <!-- 할 일 목록이 여기 표시됩니다 -->
        </ul>
    </div>
    <script src="script.js"></script>
</body>
</html>
''',

    "to_do_app/styles.css": '''body {
    font-family: Arial, sans-serif;
}

.container {
    width: 300px;
    margin: 0 auto;
    text-align: center;
}

input, button {
    margin: 10px 0;
    padding: 10px;
    width: 100%;
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    margin: 5px 0;
    padding: 10px;
    background-color: #f3f3f3;
    display: flex;
    justify-content: space-between;
}

li.completed {
    text-decoration: line-through;
    color: gray;
}
''',

    "to_do_app/script.js": '''document.getElementById('add-task-btn').addEventListener('click', function() {
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
'''
}

# 파일 생성 함수
def create_files():
    for file_name, content in files_content.items():
        # 경로가 없으면 생성
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        with open(file_name, 'w') as f:
            f.write(content)
        print(f"{file_name} 파일이 생성되었습니다.")

# 파일 생성 실행
create_files()