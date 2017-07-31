# ./binding.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2017-07-19 18:13:57.247582 by PyXB version 1.2.5 using Python 2.7.5.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:2d4b2748-6cc7-11e7-9d78-8086f2f83982')

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
    """ "adcval" means ADC values. There is one value for every receiver. In
                total 6. In the last modification of the acquisition system the type of the data was
                fixed to unsigned integer of 2 bytes. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 25, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element adcval uses Python identifier adcval
    __adcval = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'adcval'), 'adcval', '__AbsentNamespace0_CTD_ANON_adcval', True, pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 27, 16), )

    
    adcval = property(__adcval.value, __adcval.set, None, None)

    _ElementMap.update({
        __adcval.name() : __adcval
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 84, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element off uses Python identifier off
    __off = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'off'), 'off', '__AbsentNamespace0_CTD_ANON__off', True, pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 86, 16), )

    
    off = property(__off.value, __off.set, None, None)

    _ElementMap.update({
        __off.name() : __off
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


time = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'time'), pyxb.binding.datatypes.int, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 14, 4))
Namespace.addCategoryObject('elementBinding', time.name().localName(), time)

pos_time = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pos_time'), pyxb.binding.datatypes.int, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 31, 4))
Namespace.addCategoryObject('elementBinding', pos_time.name().localName(), pos_time)

azipos = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'azipos'), pyxb.binding.datatypes.int, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 36, 4))
Namespace.addCategoryObject('elementBinding', azipos.name().localName(), azipos)

elepos = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'elepos'), pyxb.binding.datatypes.int, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 41, 4))
Namespace.addCategoryObject('elementBinding', elepos.name().localName(), elepos)

pm_daz = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pm_daz'), pyxb.binding.datatypes.short, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 46, 4))
Namespace.addCategoryObject('elementBinding', pm_daz.name().localName(), pm_daz)

pm_del = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pm_del'), pyxb.binding.datatypes.short, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 51, 4))
Namespace.addCategoryObject('elementBinding', pm_del.name().localName(), pm_del)

azierr = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'azierr'), pyxb.binding.datatypes.int, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 56, 4))
Namespace.addCategoryObject('elementBinding', azierr.name().localName(), azierr)

eleerr = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'eleerr'), pyxb.binding.datatypes.int, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 61, 4))
Namespace.addCategoryObject('elementBinding', eleerr.name().localName(), eleerr)

x_off = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'x_off'), pyxb.binding.datatypes.short, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 66, 4))
Namespace.addCategoryObject('elementBinding', x_off.name().localName(), x_off)

y_off = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'y_off'), pyxb.binding.datatypes.short, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 72, 4))
Namespace.addCategoryObject('elementBinding', y_off.name().localName(), y_off)

target = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'target'), pyxb.binding.datatypes.byte, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 90, 4))
Namespace.addCategoryObject('elementBinding', target.name().localName(), target)

opmode = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'opmode'), pyxb.binding.datatypes.byte, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 101, 4))
Namespace.addCategoryObject('elementBinding', opmode.name().localName(), opmode)

gps_status = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'gps_status'), pyxb.binding.datatypes.short, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 106, 4))
Namespace.addCategoryObject('elementBinding', gps_status.name().localName(), gps_status)

recnum = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'recnum'), pyxb.binding.datatypes.int, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 111, 4))
Namespace.addCategoryObject('elementBinding', recnum.name().localName(), recnum)

adcvalVector = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'adcvalVector'), CTD_ANON, documentation=' "adcval" means ADC values. There is one value for every receiver. In\n                total 6. In the last modification of the acquisition system the type of the data was\n                fixed to unsigned integer of 2 bytes. ', location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 19, 4))
Namespace.addCategoryObject('elementBinding', adcvalVector.name().localName(), adcvalVector)

offVector = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'offVector'), CTD_ANON_, documentation='', location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 78, 4))
Namespace.addCategoryObject('elementBinding', offVector.name().localName(), offVector)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'adcval'), pyxb.binding.datatypes.unsignedShort, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 27, 16)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=6, max=6, metadata=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 27, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, 'adcval')), pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 27, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'off'), pyxb.binding.datatypes.short, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 86, 16)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=6, max=6, metadata=pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 86, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'off')), pyxb.utils.utility.Location('/home/guigue/Programming/CRAAM-Instruments/SST/SubIntegrationRBD-2002-12-13.xsd', 86, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()

