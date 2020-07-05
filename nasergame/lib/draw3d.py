import m3d

def lines(surface, color, points):
    points
    # model space -> world space
    matrix = m3d.combine([
        m3d.matrix.scale(self.scale),
        self.rotation_matrix,
        m3d.matrix.translate(self.translation),
        self.perspective_matrix
    ])
    points = m3d.transform(points, matrix)

    points = clip(points)
    # clip space -> viewport space
    points = m3d.project(points)
    # viewport space -> screen space
    points = m3d.transform(points, self.screen_matrix)
    pygame.draw.lines(screen, self.color, True, points[:,:2])
