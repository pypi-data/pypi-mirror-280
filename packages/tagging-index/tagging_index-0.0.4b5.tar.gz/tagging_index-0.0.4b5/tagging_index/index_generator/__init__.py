"""generate index in maxcompute for talent, demand, innovation etc, maxcompute should include required datasource
available index:
    TalentIndexGenerator: data from linkedin positions
    DemandIndexGenerator: data from job posting
    InnovationIndexGenerator: data from patent data 
"""

from .talent_index_generator import TalentIndexGenerator
from .demand_index_generator import DemandIndexGenerator
from .innovation_index_generator import InnovationIndexGenerator
from .index_intersection import IndexIntersection
from .common_index_generator import TIndexGenerator
