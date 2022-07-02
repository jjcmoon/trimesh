try:
    from . import generic as g
except BaseException:
    import generic as g


class VisualTest(g.unittest.TestCase):

    def test_face_subset_texture_visuals(self):
        m = g.get_mesh('fuze.obj', force='mesh')

        face_index = g.np.random.choice(len(m.faces), len(m.triangles) // 2)
        idx = m.faces[g.np.unique(face_index)].flatten()

        ori = m.visual.uv[idx]
        check = m.visual.face_subset(face_index).uv

        tree = g.spatial.cKDTree(ori)
        distances, index = tree.query(check, k=1)
        assert distances.max() < 1e-8

    def test_face_subset_color_visuals(self):
        import trimesh
        m = g.get_mesh('torus.STL')

        vertex_colors = g.np.random.randint(0, 255, size=(len(m.vertices), 3))
        m.visual = trimesh.visual.ColorVisuals(mesh=m, vertex_colors=vertex_colors)

        face_index = g.np.random.choice(len(m.faces), len(m.triangles) // 2)
        idx = m.faces[g.np.unique(face_index)].flatten()

        ori = m.visual.vertex_colors[idx]
        check = m.visual.face_subset(face_index).vertex_colors

        tree = g.spatial.cKDTree(ori)
        distances, index = tree.query(check, k=1)
        assert distances.max() < 1e-8

    # def test_face_subset_vertex_color(self):
    #     import trimesh
    #     m = g.get_mesh('torus.STL')
    #
    #     vertex_colors = trimesh.visual.VertexColor(mesh=m, vertex_color=)
    #     m.visual = trimesh.visual.VertexColor(mesh=m, colors=vertex_colors)
    #
    #     face_index = g.np.random.choice(len(m.faces), len(m.triangles) // 2)
    #     idx = m.faces[g.np.unique(face_index)].flatten()
    #
    #     ori = m.visual.vertex_colors[idx]
    #     check = m.visual.face_subset(face_index).vertex_colors
    #
    #     tree = g.spatial.cKDTree(ori)
    #     distances, index = tree.query(check, k=1)
    #     assert distances.max() < 1e-8


if __name__ == '__main__':
    g.trimesh.util.attach_to_log()
    g.unittest.main()
