/**
 * Created by joseph on 17/10/18.
 */
function addDetail(event) {
    event.preventDefault();
    $('#id_inline_detalle').append($('script[type="template/detalle"]').html());
    var num = parseInt($('#id_idventa_detventas-TOTAL_FORMS').val());
    $('[name*="__prefix__"]').each(function (i, field) {
        var name = $(this).attr('name').replace('__prefix__', num)
        $(this).attr('name', name)
        var id = $(this).attr('id').replace('__prefix__', num)
        $(this).attr('id', id)
    })
    $('[for*="__prefix__"]').each(function (i, label) {
        var name = $(this).attr('for').replace('__prefix__', num)
        $(this).attr('for', name)
    })
    $('[id*="__prefix__"]').each(function (i, obj) {
        var name = $(this).attr('id').replace('__prefix__', num)
        $(this).attr('id', name)
    })
    var total_forms = num + 1
    $('#id_idventa_detventas-TOTAL_FORMS').val(total_forms)
}
function deleteDetail(event, t) {
    event.preventDefault();
    var num = parseInt($('#id_idventa_detventas-TOTAL_FORMS').val());
    $('#id_idventa_detventas-TOTAL_FORMS').val(num - 1)
    $(t).parent().parent().parent().remove()
}

function calcularMonto(event, ths) {
    var num = $(ths).parent().parent().parent().attr('id').split('-')[1];
    var cantidad = $("#id_idventa_detventas-"+num+"-cantidad").val();
    $("#id_idventa_detventas-"+num+'-monto').val(parseInt($(ths).val())*cantidad)
}

function precioData(t) {
    var form = $(t).closest("form");
    var pk = $(t).find('option:selected').val();
    var num = $(t).parent().parent().parent().attr('id').split('-')[1];
    var data = {
        'cantidad': form.find('#id_idventa_detventas-'+num+"-cantidad").val()
    };
    $.ajax({
        url: "/ventas/articulos/"+pk+"/precio",
        data: data,
        dataType: 'json',
        success: function (data) {
            form.find('#id_idventa_detventas-'+num+'-precio').val(data['precio']);
            form.find('#id_idventa_detventas-'+num+'-monto').val(data['monto']);
            totalFact();
        }
    })
}

function totalArt() {
    var cant = 0;

    $("[id^='id_div_detalle-']").each(function (index) {
        cant += parseInt($(this).find("input[id$='cantidad']").val());
    });
    $("#id_totalarticulos").val(cant)
}

function totalFact() {
    var total = 0;

    $("[id^='id_div_detalle-']").each(function (index) {
       total += parseInt($(this).find("input[id$='monto']").val());
    });
    $("#id_totalfactura").val(total)
}