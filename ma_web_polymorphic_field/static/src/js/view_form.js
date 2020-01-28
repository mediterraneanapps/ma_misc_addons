
odoo.define('web_polymorphic_field.FieldPolymorphic', function (require) {
    var core = require('web.core');

    var FieldSelection = core.form_widget_registry.get('selection');
    var FieldPolymorphic = FieldSelection.extend( {
        template: "FieldSelection",
        init: function(field_manager, node) {
            this._super(field_manager, node);
            this.polymorphic = this.node.attrs.polymorphic;
        },
        add_polymorphism: function(reinit) {
            if(this.get_value() != false) {
                polymorphic_field = this.field_manager.fields[this.polymorphic];
                polymorphic_field.field.relation = this.get_value();
            }
        },
        render_value: function() {
            this._super();
            this.add_polymorphism();
        },
        store_dom_value: function (e) {
            this._super();
            this.add_polymorphism();
        }
    });
    core.form_widget_registry.add('polymorphic', FieldPolymorphic);
});
