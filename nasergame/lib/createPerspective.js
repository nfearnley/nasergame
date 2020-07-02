function createPerspective(fovy, near, far) {
    var aspect = 1;
    if (fovy <= 0 || fovy >= 180 || aspect <= 0 || near >= far || near <= 0) {
        throw new Error("Invalid parameters to createPerspective");
    }

    var half_fovy = self.toRadians(fovy) / 2;

    var top = near * Math.tan(half_fovy);
    var bottom = -top;
    var right = top;
    var left = -right;

    return createFrustum(left, right, bottom, top, near, far);
}

function createFrustum(width, near, far) {
    // Make sure there is no division by zero
    if (near === far) {
        throw new Error("Invalid createFrustum parameters");
    }
    if (near <= 0 || far <= 0) {
        throw new Error("For a perspective projection, the near and far distances must be positive");
    }
    if (near < far) {
        throw new Error("I guess this would be bad?");
    }
    
    var sxy = (2 * near) / width;

    var M = [
        [sxy,   0,  0,  0],
        [  0, sxy,  0,  0],
        [  0,   0,  0, -1],
        [  0,   0,  0,  0]
    ];

    return M;
};
