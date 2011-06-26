<?php

class Bewype_Accountcustomfields_Model_Resource_Eav_Mysql4_Setup extends Mage_Eav_Model_Entity_Setup
{
    public function getDefaultEntities()
    {
        return array(
            'customer' => array(
                'entity_model'          =>'customer/customer',
                'table'                 => 'customer/entity',
                'attribute_model'       => 'customer/attribute',
                'increment_model'       => 'eav/entity_increment_numeric',
                'additional_attribute_table'    => 'customer/eav_attribute',
                'entity_attribute_collection'   => 'customer/attribute_collection',
                'increment_per_store'   => false,
                'attributes' => array(
                    'clientnumber' => array(
                        'type'          => 'varchar',
                        'input'         => 'text',
                        'label'         => 'Client Number',
                        'visible'       => true,
                        'required'      => false,
                        'position'      => 80,
                    ),
                ),
            ),
        );
    }
}
