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
        sender: "server",
        receiver: name,
    })
    addMessage("[server ⇨ " + value + "]", msg,"left")
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

var last = 1;
setInterval(function(){
    var result = $.getJSON("/fetchmsg",{
        receiver:"server",
        time:last
    }).done(function(data){
        last=data.last;
        console.log(last)
        for (i=0; i < data.messages.length; i++) {
            addMessage("[" + data.messages[i].sender + " ⇨ server]", data.messages[i].message, "right")
        }
    });
},1000);