# ./rs.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2017-07-19 19:08:41.361089 by PyXB version 1.2.5 using Python 2.7.5.final.0
# Namespace AbsentNamespace0

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:d2c6e75a-6cce-11e7-b4bf-8086f2f83982')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 15, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element time uses Python identifier time
    __time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'time'), 'time', '__AbsentNamespace0_CTD_ANON_time', False, pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 17, 16), )

    
    time = property(__time.value, __time.set, None, None)

    
    # Element adcval0 uses Python identifier adcval0
    __adcval0 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'adcval0'), 'adcval0', '__AbsentNamespace0_CTD_ANON_adcval0', False, pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 18, 16), )

    
    adcval0 = property(__adcval0.value, __adcval0.set, None, None)

    
    # Element adcval1 uses Python identifier adcval1
    __adcval1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'adcval1'), 'adcval1', '__AbsentNamespace0_CTD_ANON_adcval1', False, pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 19, 16), )

    
    adcval1 = property(__adcval1.value, __adcval1.set, None, None)

    
    # Element adcval2 uses Python identifier adcval2
    __adcval2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'adcval2'), 'adcval2', '__AbsentNamespace0_CTD_ANON_adcval2', False, pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 20, 16), )

    
    adcval2 = property(__adcval2.value, __adcval2.set, None, None)

    
    # Element adcval3 uses Python identifier adcval3
    __adcval3 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'adcval3'), 'adcval3', '__AbsentNamespace0_CTD_ANON_adcval3', False, pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 21, 16), )

    
    adcval3 = property(__adcval3.value, __adcval3.set, None, None)

    
    # Element adcval4 uses Python identifier adcval4
    __adcval4 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'adcval4'), 'adcval4', '__AbsentNamespace0_CTD_ANON_adcval4', False, pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 22, 16), )

    
    adcval4 = property(__adcval4.value, __adcval4.set, None, None)

    
    # Element adcval5 uses Python identifier adcval5
    __adcval5 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'adcval5'), 'adcval5', '__AbsentNamespace0_CTD_ANON_adcval5', False, pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 23, 16), )

    
    adcval5 = property(__adcval5.value, __adcval5.set, None, None)

    
    # Element pos_time uses Python identifier pos_time
    __pos_time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pos_time'), 'pos_time', '__AbsentNamespace0_CTD_ANON_pos_time', False, pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 24, 16), )

    
    pos_time = property(__pos_time.value, __pos_time.set, None, None)

    
    # Element azipos uses Python identifier azipos
    __azipos = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'azipos'), 'azipos', '__AbsentNamespace0_CTD_ANON_azipos', False, pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 25, 16), )

    
    azipos = property(__azipos.value, __azipos.set, None, None)

    
    # Element elepos uses Python identifier elepos
    __elepos = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'elepos'), 'elepos', '__AbsentNamespace0_CTD_ANON_elepos', False, pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 26, 16), )

    
    elepos = property(__elepos.value, __elepos.set, None, None)

    
    # Element pm_daz uses Python identifier pm_daz
    __pm_daz = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pm_daz'), 'pm_daz', '__AbsentNamespace0_CTD_ANON_pm_daz', False, pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 27, 16), )

    
    pm_daz = property(__pm_daz.value, __pm_daz.set, None, None)

    
    # Element pm_del uses Python identifier pm_del
    __pm_del = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pm_del'), 'pm_del', '__AbsentNamespace0_CTD_ANON_pm_del', False, pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 28, 16), )

    
    pm_del = property(__pm_del.value, __pm_del.set, None, None)

    
    # Element azierr uses Python identifier azierr
    __azierr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'azierr'), 'azierr', '__AbsentNamespace0_CTD_ANON_azierr', False, pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 29, 16), )

    
    azierr = property(__azierr.value, __azierr.set, None, None)

    
    # Element eleerr uses Python identifier eleerr
    __eleerr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'eleerr'), 'eleerr', '__AbsentNamespace0_CTD_ANON_eleerr', False, pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 30, 16), )

    
    eleerr = property(__eleerr.value, __eleerr.set, None, None)

    
    # Element x_off uses Python identifier x_off
    __x_off = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'x_off'), 'x_off', '__AbsentNamespace0_CTD_ANON_x_off', False, pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 31, 16), )

    
    x_off = property(__x_off.value, __x_off.set, None, None)

    
    # Element y_off uses Python identifier y_off
    __y_off = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'y_off'), 'y_off', '__AbsentNamespace0_CTD_ANON_y_off', False, pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 32, 16), )

    
    y_off = property(__y_off.value, __y_off.set, None, None)

    
    # Element off0 uses Python identifier off0
    __off0 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'off0'), 'off0', '__AbsentNamespace0_CTD_ANON_off0', False, pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 33, 16), )

    
    off0 = property(__off0.value, __off0.set, None, None)

    
    # Element off1 uses Python identifier off1
    __off1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'off1'), 'off1', '__AbsentNamespace0_CTD_ANON_off1', False, pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 34, 16), )

    
    off1 = property(__off1.value, __off1.set, None, None)

    
    # Element off2 uses Python identifier off2
    __off2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'off2'), 'off2', '__AbsentNamespace0_CTD_ANON_off2', False, pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 35, 16), )

    
    off2 = property(__off2.value, __off2.set, None, None)

    
    # Element off3 uses Python identifier off3
    __off3 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'off3'), 'off3', '__AbsentNamespace0_CTD_ANON_off3', False, pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 36, 16), )

    
    off3 = property(__off3.value, __off3.set, None, None)

    
    # Element off4 uses Python identifier off4
    __off4 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'off4'), 'off4', '__AbsentNamespace0_CTD_ANON_off4', False, pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 37, 16), )

    
    off4 = property(__off4.value, __off4.set, None, None)

    
    # Element off5 uses Python identifier off5
    __off5 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'off5'), 'off5', '__AbsentNamespace0_CTD_ANON_off5', False, pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 38, 16), )

    
    off5 = property(__off5.value, __off5.set, None, None)

    
    # Element target uses Python identifier target
    __target = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'target'), 'target', '__AbsentNamespace0_CTD_ANON_target', False, pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 39, 16), )

    
    target = property(__target.value, __target.set, None, None)

    
    # Element opmode uses Python identifier opmode
    __opmode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'opmode'), 'opmode', '__AbsentNamespace0_CTD_ANON_opmode', False, pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 40, 16), )

    
    opmode = property(__opmode.value, __opmode.set, None, None)

    
    # Element gps_status uses Python identifier gps_status
    __gps_status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'gps_status'), 'gps_status', '__AbsentNamespace0_CTD_ANON_gps_status', False, pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 41, 16), )

    
    gps_status = property(__gps_status.value, __gps_status.set, None, None)

    
    # Element recnum uses Python identifier recnum
    __recnum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'recnum'), 'recnum', '__AbsentNamespace0_CTD_ANON_recnum', False, pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 42, 16), )

    
    recnum = property(__recnum.value, __recnum.set, None, None)

    _ElementMap.update({
        __time.name() : __time,
        __adcval0.name() : __adcval0,
        __adcval1.name() : __adcval1,
        __adcval2.name() : __adcval2,
        __adcval3.name() : __adcval3,
        __adcval4.name() : __adcval4,
        __adcval5.name() : __adcval5,
        __pos_time.name() : __pos_time,
        __azipos.name() : __azipos,
        __elepos.name() : __elepos,
        __pm_daz.name() : __pm_daz,
        __pm_del.name() : __pm_del,
        __azierr.name() : __azierr,
        __eleerr.name() : __eleerr,
        __x_off.name() : __x_off,
        __y_off.name() : __y_off,
        __off0.name() : __off0,
        __off1.name() : __off1,
        __off2.name() : __off2,
        __off3.name() : __off3,
        __off4.name() : __off4,
        __off5.name() : __off5,
        __target.name() : __target,
        __opmode.name() : __opmode,
        __gps_status.name() : __gps_status,
        __recnum.name() : __recnum
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


SubIntegrationRecord = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SubIntegrationRecord'), CTD_ANON, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 14, 4))
Namespace.addCategoryObject('elementBinding', SubIntegrationRecord.name().localName(), SubIntegrationRecord)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'time'), pyxb.binding.datatypes.int, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 17, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'adcval0'), pyxb.binding.datatypes.unsignedShort, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 18, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'adcval1'), pyxb.binding.datatypes.unsignedShort, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 19, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'adcval2'), pyxb.binding.datatypes.unsignedShort, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 20, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'adcval3'), pyxb.binding.datatypes.unsignedShort, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 21, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'adcval4'), pyxb.binding.datatypes.unsignedShort, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 22, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'adcval5'), pyxb.binding.datatypes.unsignedShort, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 23, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pos_time'), pyxb.binding.datatypes.int, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 24, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'azipos'), pyxb.binding.datatypes.int, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 25, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'elepos'), pyxb.binding.datatypes.int, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 26, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pm_daz'), pyxb.binding.datatypes.short, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 27, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pm_del'), pyxb.binding.datatypes.short, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 28, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'azierr'), pyxb.binding.datatypes.int, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 29, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'eleerr'), pyxb.binding.datatypes.int, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 30, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'x_off'), pyxb.binding.datatypes.short, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 31, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'y_off'), pyxb.binding.datatypes.short, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 32, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'off0'), pyxb.binding.datatypes.short, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 33, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'off1'), pyxb.binding.datatypes.short, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 34, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'off2'), pyxb.binding.datatypes.short, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 35, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'off3'), pyxb.binding.datatypes.short, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 36, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'off4'), pyxb.binding.datatypes.short, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 37, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'off5'), pyxb.binding.datatypes.short, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 38, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'target'), pyxb.binding.datatypes.byte, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 39, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'opmode'), pyxb.binding.datatypes.byte, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 40, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'gps_status'), pyxb.binding.datatypes.short, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 41, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'recnum'), pyxb.binding.datatypes.int, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 42, 16)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'time')), pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 17, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'adcval0')), pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 18, 16))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'adcval1')), pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 19, 16))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'adcval2')), pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 20, 16))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'adcval3')), pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 21, 16))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'adcval4')), pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 22, 16))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'adcval5')), pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 23, 16))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'pos_time')), pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 24, 16))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'azipos')), pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 25, 16))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'elepos')), pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 26, 16))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'pm_daz')), pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 27, 16))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'pm_del')), pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 28, 16))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'azierr')), pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 29, 16))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'eleerr')), pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 30, 16))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'x_off')), pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 31, 16))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'y_off')), pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 32, 16))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'off0')), pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 33, 16))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'off1')), pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 34, 16))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'off2')), pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 35, 16))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'off3')), pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 36, 16))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'off4')), pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 37, 16))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'off5')), pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 38, 16))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'target')), pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 39, 16))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'opmode')), pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 40, 16))
    st_23 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'gps_status')), pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 41, 16))
    st_24 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'recnum')), pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 42, 16))
    st_25 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
         ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
         ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
         ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
         ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
         ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
         ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
         ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
         ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
         ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
         ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
         ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
         ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_25, [
         ]))
    st_24._set_transitionSet(transitions)
    transitions = []
    st_25._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()

