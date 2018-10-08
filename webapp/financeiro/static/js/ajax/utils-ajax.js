let server = $("#server").val();
let csrftoken = getCookie('csrftoken');

$("#btn-add").click(() => {
    $("#form-item").submit((e) => {
        onSaveClick();
        e.preventDefault();
    });
});

onEditClick = (element) => {
    // Habilitando o formulário
    $("#save").show();
    $("input").attr('disabled', false);
    $("select").attr('disabled', false);

    // Recuperando as informações do registro
    let id_item = $(element).attr('item-id');

    let ajax = requestView(id_item);

    ajax.always((response) => {

        if (response.status === 200 && response.readyState === 4) {
            json = JSON.parse(response.responseText);

            for (let key in json)
                $("[name='" + key + "']").val(json[key]);

            // Definindo ação no click do botão save
            $("#form-item").submit((e) => {
                onSaveClick(id_item);
                e.preventDefault();
            });
        }
        else {

        }

    });

}

onViewClick = (element) => {
    // Desabilitando o formulário
    $("#save").hide();
    $("input").attr('disabled', true);
    $("select").attr('disabled', true);

    // Recuperando as informações do registro
    let id_item = $(element).attr('item-id');

    let ajax = requestView(id_item);

    ajax.always((response) => {
        if (response.status === 200 && response.readyState === 4) {
            json = JSON.parse(response.responseText);

            for (let key in json)
                $("[name='" + key + "']").val(json[key]);
        }
        else {

        }
    });
}

onSaveClick = (id_item = null) => {
    let form = prepareDataRequest($('#form-item').serializeArray());

    let ajax = (id_item == null) ? requestAdd(form) : requestEdit(id_item, form);

    ajax.always((response) => {
        if (response.status === 200 && response.readyState === 4) {
            console.log(response.responseText);
        }
        else {
            console.log(response.responseText);
        }
    });

}

onDeleteClick = (element) => {
    // Recuperando as informações do registro
    let id_item = $(element).attr('item-id');

    let ajax = requestDelete(id_item);

    ajax.always((response) => {
        if (response.status === 200 && response.readyState === 4) {
            window.location.reload();
        }
        else {
            console.log(response.responseText);
        }
    });
}

prepareDataRequest = (data) => {
    let new_data = {};

    for (let i in data)
        new_data[data[i]["name"]] = data[i]["value"];

    return new_data;
}

// view request
requestView = (id_item) => {
    return request("GET", "view", id_item);
}

// add request
requestAdd = (data) => {
    return request("POST", "add", null, data);
}

// edit request
requestEdit = (id_item, data) => {
    return request("POST", "edit", id_item, data);
}

// delete request
requestDelete = (id_item) => {
    return request("DELETE", "delete", id_item);
}

// generic request
request = (type, action, id_item, data = null) => {
    let url = server + "/" + $("#model").val() + "/" + action;
    url += (id_item != null) ? "/" + id_item : "/";
    return $.ajax({
        type: type,
        url: url,
        dataType: "json/application",
        data: (data != null) ? {"form": JSON.stringify(data)} : {}
    });
}

// using jQuery
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});