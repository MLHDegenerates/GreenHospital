function onSend() {
    var value = $("#recipient").val();
    var name = $("#stafflist [value='" + value + "']").attr('data-value');
    var msg = $("#messagebox").val();
    console.log(value);
    console.log(name);
    if (name == undefined) {
        alert("Name not found");
        return;
    }
    $.getJSON("/sendmsg",{
        message: msg,
        username: name
    })
    addMessage(value, msg,"left")
}

function addMessage(user, text, side) {
    var line = $("<div></div>")
        .append(
            $("<span>" + user + "</span>")
            .css("text-align","left")
            .css("padding-right","10px")
        )
        .append(
            $("<span>" + text + "</span>")
            .css("text-align",side)
        )
        .css("text-align","left")
        .appendTo(".container-messages")
}

var last = 0;

setInterval(function(){
    var result = $.getJSON("/fetchmsg",{
        username:"server",
        time:last
    }).done(function(data){
        last=data.last;
        for (msg in data.messages) {
            addMessage("yik",msg,"right")
        }
    });
},1000);