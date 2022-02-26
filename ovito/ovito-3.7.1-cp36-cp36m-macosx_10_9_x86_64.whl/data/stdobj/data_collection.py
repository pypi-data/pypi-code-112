# Load dependencies
import ovito
from ovito.data import DataCollection
from ovito.data.data_objects_dict import DataObjectsDict

# Load the native code module
from ovito.plugins.StdObjPython import SimulationCell, DataTable

# Implementation of the DataCollection.tables attribute.
def _DataCollection_tables(self):
    """
    A dictionary view of all :py:class:`DataTable` objects in
    this data collection. Each :py:class:`DataTable` has a unique :py:attr:`~ovito.data.DataObject.identifier` key, 
    which can be used to look it up in this dictionary. You can use

    .. literalinclude:: ../example_snippets/data_collection_tables.py
        :lines: 9-9

    to find out which table identifiers exist in the dictionary. Modifiers that generate a data table typically 
    assign a predefined identifier, which can be found in their documentation.
    Use the key string to retrieve the desired :py:class:`DataTable` from the dictionary, e.g.

    .. literalinclude:: ../example_snippets/data_collection_tables.py
        :lines: 14-15

    """
    return DataObjectsDict(self, DataTable)
DataCollection.tables = property(_DataCollection_tables)

# Implementation of the DataCollection.cell attribute.
def _DataCollection_cell(self):
    """ 
    Returns the :py:class:`SimulationCell` object, which stores the cell vectors and periodic boundary
    condition flags, or ``None`` if there is no cell information associated with this data collection. 

    Note: The :py:class:`SimulationCell` data object may be read-only if it is currently shared by
    several data collections. Use the :py:attr:`!cell_` field instead to request a mutable cell object 
    if you intend to modify it.
    """
    return self.find(SimulationCell)
# Implement the assignment of a SimulationCell object to the DataCollection.cell field.
def _DataCollection_set_cell(self, obj):
    assert(obj is None or isinstance(obj, SimulationCell)) # Must assign a SimulationCell data object to this field.
    # Check if there already is an existing SimulationCell object in the DataCollection. 
    # If yes, first remove it from the collection before adding the new one. 
    existing = self.find(SimulationCell)
    if existing is not obj:
        if not existing is None: self.remove(existing)
        if not obj is None: self.objects.append(obj)
DataCollection.cell = property(_DataCollection_cell, _DataCollection_set_cell)

# Implementation of the DataCollection.cell_ attribute.
DataCollection.cell_ = property(lambda self: self.make_mutable(self.cell), _DataCollection_set_cell)

# For backward compatibility with development versions of OVITO 3.0:
DataCollection.series = property(lambda self: self.tables)
