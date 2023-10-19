import open3d as o3d


pcd = o3d.t.io.read_point_cloud('test_ascii.pcd')
print(pcd.point.positions.numpy())
o3d.t.io.write_point_cloud('copt_binary.pcd', pcd, compressed=True)
