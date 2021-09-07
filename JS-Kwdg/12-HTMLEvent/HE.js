function showAlert() {
    alert("showing message:\nOh,visitor!")
}

let bottom_m = document.getElementById("testButtom1")
//搜索对应ID元素并将结果给变量（网页中的对应元素是按钮标签）
bottom_m.onclick = showAlert()
//设置处理程序，但只能处理一个事件
//示例程序在此可能有一个BUG

function showHEY() {
    alert("Hey,\nBro!")
}

let bottom_listen = document.getElementById("testBottom2");
bottom_listen.addEventListener("click", showAlert)
bottom_listen.addEventListener("click", showHEY)

//bottom_listen.removeEventListener("click", showAlert)
//删除shijian监听器

function clickCoordinate (event) {
    alert(`Click coordinate: ${event.clientX} - ${event.clientY}`)
    console.log(event)
}
let findEvOb = document.getElementById("textEventObject")
findEvOb.addEventListener("click", clickCoordinate)
