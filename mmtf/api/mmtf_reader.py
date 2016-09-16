from mmtf.codecs import decode_array
from mmtf.utils import decoder_utils
import sys


class MMTFDecoder():
    """Class to decode raw mmtf data into a parsed data model that can be fed into other data model"""
    model_counter = 0
    chain_counter = 0
    group_counter = 0
    atom_counter = 0


    def get_coords(self):
        """Utility function to get the coordinates as a single list of tuples."""
        out_list = []
        for i in range(len(self.x_coord_list)):
            out_list.append((self.x_coord_list[i],self.y_coord_list[i],self.z_coord_list,))
        return out_list

    def get_bonds(self):
        """Utility function to get all the inter group bonds for the structure in pairs."""
        return decoder_utils.get_bonds(self)

    def decode_data(self, input_data):
        """Function to decode the input data and place it onto the class.
        :param input_data: the input data as a dict"""
        self.group_type_list = decode_array(input_data[b"groupTypeList"])
        self.x_coord_list = decode_array(input_data[b"xCoordList"])
        self.y_coord_list = decode_array(input_data[b"yCoordList"])
        self.z_coord_list = decode_array(input_data[b"zCoordList"])
        if b"bFactorList" in input_data:
            self.b_factor_list = decode_array(input_data[b"bFactorList"])
        else:
            self.b_factor_list = []
        if b"occupancyList" in input_data:
            self.occupancy_list = decode_array(input_data[b"occupancyList"])
        else:
            self.occupancy_list = []
        if b"atomIdList" in input_data:
            self.atom_id_list = decode_array(input_data[b"atomIdList"])
        else:
            self.atom_id_list = []
        if b"altLocList" in input_data:
            self.alt_loc_list = decode_array(input_data[b"altLocList"])
        else:
            self.alt_loc_list = []
        if b"insCodeList" in input_data:
            self.ins_code_list = decode_array(input_data[b"insCodeList"])
        else:
            self.ins_code_list = []
        self.group_id_list = decode_array(input_data[b"groupIdList"])
        self.group_list = decoder_utils.decode_group_map(input_data[b"groupList"])
        if b"sequenceIndexList" in input_data:
            self.sequence_index_list = decode_array(input_data[b"sequenceIndexList"])
        else:
            self.sequence_index_list = []
        self.chains_per_model = input_data[b"chainsPerModel"]
        self.groups_per_chain = input_data[b"groupsPerChain"]
        if b"chainNameList" in input_data:
            self.chain_name_list = decode_array(input_data[b"chainNameList"])
        else:
            self.chain_name_list = []
        self.chain_id_list = decode_array(input_data[b"chainIdList"])
        if b"spaceGroup" in input_data:
            self.space_group = input_data[b"spaceGroup"]
        else:
            self.space_group = None
        if b"bondAtomList" in input_data:
            self.bond_atom_list = decode_array(input_data[b"bondAtomList"])
        else:
            self.bond_atom_list = None
        if b"bondOrderList" in input_data:
            self.bond_order_list = decode_array(input_data[b"bondOrderList"])
        else:
            self.bond_order_list = None
        if sys.version_info[0] < 3:
            if b"mmtfVersion" in input_data:
                self.mmtf_version = input_data[b"mmtfVersion"]
            else:
                self.mmtf_version = None
            if b"mmtfProducer" in input_data:
                self.mmtf_producer = input_data[b"mmtfProducer"]
            else:
                self.mmtf_producer = None
            if b"structureId" in input_data:
                self.structure_id = input_data[b"structureId"]
            else:
                self.structure_id = None
        else:
            if b"mmtfVersion" in input_data:
                self.mmtf_version = input_data[b"mmtfVersion"].decode('ascii')
            else:
                self.mmtf_version = None
            if b"mmtfProducer" in input_data:
                self.mmtf_producer = input_data[b"mmtfProducer"].decode('ascii')
            else:
                self.mmtf_producer = None
            if b"structureId" in input_data:
                self.structure_id = input_data[b"structureId"].decode('ascii')
            else:
                self.structure_id = None
        if b"title" in input_data:
            if sys.version_info[0] < 3:
                self.title = input_data[b"title"]
            else:
                self.title = input_data[b"title"].decode('ascii')
        if b"experimentalMethods" in input_data:
            if sys.version_info[0] < 3:
                self.experimental_methods = [x.decode('ascii') for x in input_data[b"experimentalMethods"]]
            else:
                self.experimental_methods = input_data[b"experimentalMethods"]
        else:
            self.experimental_methods = None
        if b"depositionDate" in input_data:
            if sys.version_info[0] < 3:
                self.deposition_date = input_data[b"depositionDate"]
            else:
                self.deposition_date = input_data[b"depositionDate"].decode('ascii')
        else:
            self.deposition_date = None
        if b"releaseDate" in input_data:
            if sys.version_info[0] < 3:
                self.release_date = input_data[b"releaseDate"]
            else:
                self.release_date = input_data[b"releaseDate"].decode('ascii')
        else:
            self.release_date = None
        if b"entityList" in input_data:
            self.entity_list = decoder_utils.decode_entity_list(input_data[b"entityList"])
        else:
            self.entity_list = []
        if b"bioAssemblyList" in input_data:
            self.bio_assembly = input_data[b"bioAssemblyList"]
        else:
            self.bio_assembly = []
        if b"rFree" in input_data:
            self.r_free = input_data[b"rFree"]
        else:
            self.r_free = None
        if b"rWork" in input_data:
            self.r_work = input_data[b"rWork"]
        else:
            self.r_work = None
        if b"resolution" in input_data:
            self.resolution = input_data[b"resolution"]
        else:
            self.resolution = None
        if b"unitCell" in input_data:
            self.unit_cell = input_data[b"unitCell"]
        else:
            self.unit_cell = None
        if b"secStructList" in input_data:
            self.sec_struct_list = decode_array(input_data[b"secStructList"])
        # Now all the numbers to defien the
        self.num_bonds = int(input_data[b"numBonds"])
        self.num_chains = int(input_data[b"numChains"])
        self.num_models = int(input_data[b"numModels"])
        self.num_atoms = int(input_data[b"numAtoms"])
        self.num_groups = int(input_data[b"numGroups"])


    def pass_data_on(self, data_setters):
        """Write the data from the getters to the setters.

        :param data_setters: a series of functions that can fill a chemical
        data structure
        :type data_setters: DataTransferInterface
        """
        data_setters.init_structure(self.num_bonds, len(self.x_coord_list), len(self.group_type_list),
                                    len(self.chain_id_list), len(self.chains_per_model), self.structure_id)
        decoder_utils.add_entity_info(self, data_setters)
        decoder_utils.add_atomic_information(self, data_setters)
        decoder_utils.add_header_info(self, data_setters)
        decoder_utils.add_xtalographic_info(self, data_setters)
        decoder_utils.generate_bio_assembly(self, data_setters)
        decoder_utils.add_inter_group_bonds(self, data_setters)
        data_setters.finalize_structure()