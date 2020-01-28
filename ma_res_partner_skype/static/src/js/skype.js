
odoo.define('res_partner_skype.widget', function (require) {
'use strict';


var fieldRegistry = require('web.field_registry');
var basicFields = require('web.basic_fields');
var FieldEmail = basicFields.FieldEmail;


var FieldSkype = FieldEmail.extend({
    description: "skype",
    prefix: 'skype',

    _renderReadonly: function() {
        this.$el.text(this.value)
            .addClass('o_form_uri o_text_overflow')
            .attr('href', this.prefix + ':' + this.value + '?call');
    },
});

fieldRegistry.add('skype', FieldSkype);

});
