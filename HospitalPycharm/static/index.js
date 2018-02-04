function onSend() {
//    console.log("yeet")
//    #.getJSON("/sendmsg",{
//        message: "ohno",
//
//    })
    var value = $("#recipient").val();
    console.log(value)
    console.log(
    $("#stafflist [value='" + value + "']").attr('data-value')
    )
}