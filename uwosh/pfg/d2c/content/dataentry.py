from AccessControl import ClassSecurityInfo
from Products.ATContentTypes.content.base import registerATCT
from uwosh.pfg.d2c.config import PROJECTNAME
from Products.ATContentTypes.content.base import ATCTContent
from Products.ATContentTypes.content.schemata import ATContentTypeSchema
from uwosh.pfg.d2c.interfaces import IFormSaveData2ContentEntry
from zope.interface import implements

FormSaveData2ContentEntrySchema = ATContentTypeSchema.copy()
FormSaveData2ContentEntrySchema.delField('title')
FormSaveData2ContentEntrySchema.delField('description')

class FormSaveData2ContentEntry(ATCTContent):
    implements(IFormSaveData2ContentEntry)
    
    schema = FormSaveData2ContentEntrySchema

    meta_type = portal_type = 'FormSaveData2ContentEntry'
    archetype_name = 'Save Data to Content Entry'
    
    security       = ClassSecurityInfo()
    
    def Title(self):
        field = self.getParentNode().getTitleField()
        schema = self.Schema()
        if schema.has_key(field):
            value = schema.get(field).get(self)
            try:
                if not isinstance(value, basestring):
                    # not of string type so convert it
                    # This may not always work but might prevent some errors.
                    value = str(value)
            except:
                pass
            
            return value
        else:
            return self.getId()
        
    security.declareProtected('View', 'getValue')
    def getValue(self, field):
        """
        somewhat a replacement for the get generated methods.
        """
        schema = self.Schema()
        field = schema.get(field)
        return field.get(self)
        
    
registerATCT(FormSaveData2ContentEntry, PROJECTNAME)
