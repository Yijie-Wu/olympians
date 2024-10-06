let api_server = 'http://127.0.0.1:8000'

export function calcAvatar(avatar = 'avatar.png') {
    const timestamp = Date.now().toString();
    return `${api_server}/user/avatar/${avatar}` + '?t=' + timestamp
}

export function calcAvatarByID(id) {
    const timestamp = Date.now().toString();
    return 'http://127.0.0.1:8000/user/avatar/id/' + id + '?t=' + timestamp
}

export function calcFile(image, file_type = 'file') {
    const timestamp = Date.now().toString();
    return `${api_server}/download/${file_type}/${image}` + '?t=' + timestamp
}

export function JSON_Validate(json) {
    try {
        JSON.parse(json)
        return true
    } catch (e) {
        return false
    }
}
