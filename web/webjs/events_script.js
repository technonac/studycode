/**
 *  load：当页面完全加载后在 window 上面触发，当所有框架都加载完毕时在框架集上面触发，
 *  当图像加载完毕时在<img>元素上面触发，或者当嵌入的内容加载完毕时在<object>元素上面
 *  触发。
 */
window.onload = function () {
    //dom0
    var btn = document.getElementById("btn");
    btn.onclick = function () {
        console.log(event.type);
    };

    //dom2
    var handler = function () {
        console.log("btn id = " + this.id);
        console.log("--- event attributes ---");
        console.log("bubbles = " + event.bubbles);
        console.log("cancelable = " + event.cancelable);
        console.log("currentTarget = " + event.currentTarget);
        console.log("defaultPrevented = " + event.defaultPrevented);
        console.log("eventPhase = " + event.eventPhase); //调用事件处理程序的阶段： 1表示捕获阶段， 2表示“处于目标”， 3表示冒泡阶段
        console.log("target = " + event.target);

        console.log(event.currentTarget === this); //true
        console.log(event.target === this); //true

        console.log("screen coordinates = " + event.screenX + " , " + event.screenY);
        console.log("client coordinates = " + event.clientX + " , " + event.clientY);
        console.log("page coordinates = " + event.pageX + " , " + event.pageY);
        console.log("shiftKey = " + event.shiftKey);
        console.log("ctrlKey = " + event.ctrlKey);
        console.log("altKey = " + event.altKey);
        console.log("metaKey = " + event.metaKey); //window(win) or cmd(mac)
        console.log("detail = " + event.detail); //同一位置点击次数


        event.stopPropagation();
    };
    btn.addEventListener('click', handler, false);
    // btn.removeEventListener('click', handler, false);

    window.addEventListener("resize", function () {
        // console.log("width,height = " + window.innerHeight + " , " + window.innerWidth);
    })


    var mydiv = document.getElementById("mydiv");
    mydiv.addEventListener("mousedown", function () {
        console.log("button = " + event.button);
    });

    /**
     * 向前 120 向后-120
     */
    document.addEventListener("mousewheel", function () {
        console.log(event.wheelDelta);
    });

    var input = document.getElementById("input");
    input.addEventListener("keypress", function () {
        console.log("keyCode = " + event.keyCode + ",charCode = " + event.charCode + ",key = " + event.key);
    });

    input.addEventListener("textInput", function () {
        console.log("data = " + event.data);
    });

    var event = document.createElement("UIEvent");
    
};


/**
 * 兼容性添加事件处理
 * @type {{addHandler: EventUtil.addHandler, removeHandler: EventUtil.removeHandler}}
 */
var EventUtil = {
    addHandler: function (element, type, handler) {
        if (element.addEventListener) {
            element.addEventListener(type, handler, false);
        } else if (element.attachEvent) {
            element.attachEvent(type, handler);
        } else {
            element["on" + type] = handler;
        }
    },
    removeHandler: function (element, type, handler) {
        if (element.removeEventListener) {
            element.removeEventListener(type, handler, false);
        } else if (element.detachEvent) {
            element.detachEvent("on" + type, handler);
        } else {
            element["on" + type] = null;
        }
    }
};