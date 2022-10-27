var item1 = $("<li></li>").text("Item");

$('#add_item').click(function() {
   $('.my_list').append(item1)
})