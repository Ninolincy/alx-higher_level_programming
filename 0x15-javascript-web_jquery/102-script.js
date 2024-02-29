#!/usr/bin/node
$(document).ready(function() {
  $('#btn_translate').click(function() {
    const languageCode = $('#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/hello/${languageCode}`;

    $.get(url, function(translation) {
      $('#hello').text(translation.hello);
    });
  });
});
