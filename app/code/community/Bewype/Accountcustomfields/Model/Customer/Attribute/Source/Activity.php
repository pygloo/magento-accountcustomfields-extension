<?php

class Bewype_Accountcustomfields_Model_Customer_Attribute_Source_Activity extends Mage_Eav_Model_Entity_Attribute_Source_Table
{
    public function getAllOptions()
    {
        if (!$this->_options)
        {
            $this->_options = array(
                array(
                    'value' => '',
                    'label' => '',
                ),
                array(
                    'value' => '1',
                    'label' => 'Grossiste revendeur',
                ),
                array(
                    'value' => '2',
                    'label' => 'Installateur',
                ),
                array(
                    'value' => '3',
                    'label' => 'Administration',
                ),
                array(
                    'value' => '4',
                    'label' => 'Collectivités',
                ),
                array(
                    'value' => '5',
                    'label' => 'Hôtel, Restaurant',
                ),
                array(
                    'value' => '6',
                    'label' => 'Architecte, Bureau d\'études',
                ),
                array(
                    'value' => '7',
                    'label' => 'Etudiant',
                ),
                array(
                    'value' => '8',
                    'label' => 'Société de nettoyage',
                ),
                array(
                    'value' => '9',
                    'label' => 'Particulier',
                ),
            );
        }
        return $this->_options;
    }
}

