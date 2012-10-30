#!/usr/bin/python

class output(object):
	def __str__(self):
		return str(self.__dict__)


class flavor(output):
	"""
+----+-----------+-----------+------+-----------+------+-------+-------------+
| ID |    Name   | Memory_MB | Disk | Ephemeral | Swap | VCPUs | RXTX_Factor |
+----+-----------+-----------+------+-----------+------+-------+-------------+
| 1  | m1.tiny   | 512       | 0    | 0         |      | 1     | 1.0         |
| 2  | m1.small  | 2048      | 10   | 20        |      | 1     | 1.0         |
| 3  | m1.medium | 4096      | 10   | 40        |      | 2     | 1.0         |
| 4  | m1.large  | 8192      | 10   | 80        |      | 4     | 1.0         |
| 5  | m1.xlarge | 16384     | 10   | 160       |      | 8     | 1.0         |
+----+-----------+-----------+------+-----------+------+-------+-------------+
	"""
	def __init__(self, line):
		items = line.split("|")
		if len(items) < 9:
			return
		self.ID=items[1].strip()
		self.Name=items[2].strip()
		self.Memory_MB=items[3].strip()
		self.Disk=items[4].strip()
		self.Ephemeral=items[5].strip()
		self.Swap=items[6].strip()
		self.VCPUs=items[7].strip()
		self.RXTX_Factor=items[8].strip()

class image(output):
	"""
+--------------------------------------+---------------------------------+--------+--------+
|                  ID                  |               Name              | Status | Server |
+--------------------------------------+---------------------------------+--------+--------+
| 20b43fa7-0fc2-4bb3-aeec-fa7a4feb86c4 | cirros-0.3.0-x86_64-uec-ramdisk | ACTIVE |        |
| 48e81475-efbd-487d-9f58-70acc250d4f4 | cirros-0.3.0-x86_64-uec-kernel  | ACTIVE |        |
| a0bfe180-8d76-40d5-b898-238eccbdcbf1 | cirros-0.3.0-x86_64-uec         | ACTIVE |        |
+--------------------------------------+---------------------------------+--------+--------+
	"""
	def __init__(self, line):
		items = line.split("|")
		if len(items) < 5:
			print "error parsing line"
			return
		self.ID=items[1].strip()
		self.Name=items[2].strip()
		self.Status=items[3].strip()
		self.Server=items[4].strip()

class vm(output):
	"""
+--------------------------------------+---------+--------+--------------------+
|                  ID                  |   Name  | Status |      Networks      |
+--------------------------------------+---------+--------+--------------------+
| 80818e92-7b15-4b22-a7d4-7eebe94941e0 | cmdtest | ACTIVE | private=10.10.10.4 |
+--------------------------------------+---------+--------+--------------------+
"""
	def __init__(self, line):
		items = line.split("|")
		self.ID=items[1].strip()
		self.Name=items[2].strip()
		self.Status=items[3].strip()
		self.Networks=items[4].strip()

class volume(output):
	"""
+----+-----------+--------------+------+-------------+-------------+
| ID |   Status  | Display Name | Size | Volume Type | Attached to |
+----+-----------+--------------+------+-------------+-------------+
| 2  | available | testvolume1  | 5    | None        |             |
+----+-----------+--------------+------+-------------+-------------+
	"""
	def __init__(self, line):
		items = line.split("|")
		if len(items) < 7:
			return
		self.ID=items[1].strip()
		self.Status=items[2].strip()
		self.Name=items[3].strip()
		self.Size=items[4].strip()
		self.Type=items[5].strip()
		self.Attachedto=items[6].strip()

def main():
	f = flavor(r"| 1  | m1.tiny   | 512       | 0    | 0         |      | 1     | 1.0         |")
	print f

if __name__ == "__main__":
	main()
