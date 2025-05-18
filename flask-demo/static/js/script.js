// 以下是几种不同类型弹出交互对话框的例子

// 警告对话框，显示一条消息并带有一个确认按钮
function showAlertDialog() {
    alert('这是一个警告对话框示例，点击确定继续。');
}

// 确认对话框，显示一条消息并带有确认和取消按钮，返回布尔值表示用户选择
function showConfirmDialog() {
    const result = confirm('这是一个确认对话框示例，你是否要继续？');
    if (result) {
        console.log('用户点击了确认按钮');
    } else {
        console.log('用户点击了取消按钮');
    }
}

// 提示对话框，显示一条消息并带有一个输入框和确认、取消按钮
function showPromptDialog() {
    const input = prompt('这是一个提示对话框示例，请输入你的姓名：');
    if (input !== null) {
        console.log('你输入的姓名是：' + input);
    } else {
        console.log('你点击了取消按钮');
    }
}

// 调用示例
// showAlertDialog();
// showConfirmDialog();
// showPromptDialog();
