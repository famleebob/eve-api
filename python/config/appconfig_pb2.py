# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config/appconfig.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from evecommon import acipherinfo_pb2 as evecommon_dot_acipherinfo__pb2
from config import devcommon_pb2 as config_dot_devcommon__pb2
from config import storage_pb2 as config_dot_storage__pb2
from config import vm_pb2 as config_dot_vm__pb2
from config import netconfig_pb2 as config_dot_netconfig__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x63onfig/appconfig.proto\x12\x15org.lfedge.eve.config\x1a\x1b\x65vecommon/acipherinfo.proto\x1a\x16\x63onfig/devcommon.proto\x1a\x14\x63onfig/storage.proto\x1a\x0f\x63onfig/vm.proto\x1a\x16\x63onfig/netconfig.proto\"2\n\x0eInstanceOpsCmd\x12\x0f\n\x07\x63ounter\x18\x02 \x01(\r\x12\x0f\n\x07opsTime\x18\x04 \x01(\t\"M\n\x0cSnapshotDesc\x12\n\n\x02id\x18\x01 \x01(\t\x12\x31\n\x04type\x18\x02 \x01(\x0e\x32#.org.lfedge.eve.config.SnapshotType\"\xb5\x01\n\x0eSnapshotConfig\x12\x17\n\x0f\x61\x63tive_snapshot\x18\x01 \x01(\t\x12;\n\x0crollback_cmd\x18\x02 \x01(\x0b\x32%.org.lfedge.eve.config.InstanceOpsCmd\x12\x15\n\rmax_snapshots\x18\x03 \x01(\r\x12\x36\n\tsnapshots\x18\x04 \x03(\x0b\x32#.org.lfedge.eve.config.SnapshotDesc\"\xc6\x07\n\x11\x41ppInstanceConfig\x12=\n\x0euuidandversion\x18\x01 \x01(\x0b\x32%.org.lfedge.eve.config.UUIDandVersion\x12\x13\n\x0b\x64isplayname\x18\x02 \x01(\t\x12\x37\n\x0e\x66ixedresources\x18\x03 \x01(\x0b\x32\x1f.org.lfedge.eve.config.VmConfig\x12,\n\x06\x64rives\x18\x04 \x03(\x0b\x32\x1c.org.lfedge.eve.config.Drive\x12\x10\n\x08\x61\x63tivate\x18\x05 \x01(\x08\x12\x39\n\ninterfaces\x18\x06 \x03(\x0b\x32%.org.lfedge.eve.config.NetworkAdapter\x12\x30\n\x08\x61\x64\x61pters\x18\x07 \x03(\x0b\x32\x1e.org.lfedge.eve.config.Adapter\x12\x36\n\x07restart\x18\t \x01(\x0b\x32%.org.lfedge.eve.config.InstanceOpsCmd\x12\x34\n\x05purge\x18\n \x01(\x0b\x32%.org.lfedge.eve.config.InstanceOpsCmd\x12\x10\n\x08userData\x18\x0b \x01(\t\x12\x15\n\rremoteConsole\x18\x0c \x01(\x08\x12\x36\n\ncipherData\x18\r \x01(\x0b\x32\".org.lfedge.eve.common.CipherBlock\x12\x1a\n\x12\x63ollectStatsIPAddr\x18\x0f \x01(\t\x12\x37\n\rvolumeRefList\x18\x10 \x03(\x0b\x32 .org.lfedge.eve.config.VolumeRef\x12\x39\n\x0cmetaDataType\x18\x11 \x01(\x0e\x32#.org.lfedge.eve.config.MetaDataType\x12\x14\n\x0cprofile_list\x18\x12 \x03(\t\x12\x1e\n\x16start_delay_in_seconds\x18\x13 \x01(\r\x12\x0f\n\x07service\x18\x14 \x01(\x08\x12\x1a\n\x12\x63loud_init_version\x18\x15 \x01(\r\x12\x37\n\x08snapshot\x18\x16 \x01(\x0b\x32%.org.lfedge.eve.config.SnapshotConfig\x12\x39\n\x08patchRef\x18\x17 \x01(\x0b\x32\'.org.lfedge.eve.config.PatchEnvelopeRef\x12\x19\n\x11\x61llow_to_discover\x18\x19 \x01(\x08\x12\x1a\n\x12\x64\x65signated_node_id\x18\x1a \x01(\tJ\x04\x08\x0e\x10\x0fJ\x04\x08\x18\x10\x19\",\n\x10PatchEnvelopeRef\x12\x0c\n\x04name\x18\x17 \x01(\t\x12\n\n\x02id\x18\x18 \x01(\t\"E\n\tVolumeRef\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x17\n\x0fgenerationCount\x18\x02 \x01(\x03\x12\x11\n\tmount_dir\x18\x03 \x01(\t*f\n\x0cMetaDataType\x12\x11\n\rMetaDataDrive\x10\x00\x12\x10\n\x0cMetaDataNone\x10\x01\x12\x15\n\x11MetaDataOpenStack\x10\x02\x12\x1a\n\x16MetaDataDriveMultipart\x10\x03*K\n\x0cSnapshotType\x12\x1d\n\x19SNAPSHOT_TYPE_UNSPECIFIED\x10\x00\x12\x1c\n\x18SNAPSHOT_TYPE_APP_UPDATE\x10\x01\x42=\n\x15org.lfedge.eve.configZ$github.com/lf-edge/eve-api/go/configb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'config.appconfig_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\025org.lfedge.eve.configZ$github.com/lf-edge/eve-api/go/config'
  _globals['_METADATATYPE']._serialized_start=1566
  _globals['_METADATATYPE']._serialized_end=1668
  _globals['_SNAPSHOTTYPE']._serialized_start=1670
  _globals['_SNAPSHOTTYPE']._serialized_end=1745
  _globals['_INSTANCEOPSCMD']._serialized_start=165
  _globals['_INSTANCEOPSCMD']._serialized_end=215
  _globals['_SNAPSHOTDESC']._serialized_start=217
  _globals['_SNAPSHOTDESC']._serialized_end=294
  _globals['_SNAPSHOTCONFIG']._serialized_start=297
  _globals['_SNAPSHOTCONFIG']._serialized_end=478
  _globals['_APPINSTANCECONFIG']._serialized_start=481
  _globals['_APPINSTANCECONFIG']._serialized_end=1447
  _globals['_PATCHENVELOPEREF']._serialized_start=1449
  _globals['_PATCHENVELOPEREF']._serialized_end=1493
  _globals['_VOLUMEREF']._serialized_start=1495
  _globals['_VOLUMEREF']._serialized_end=1564
# @@protoc_insertion_point(module_scope)
