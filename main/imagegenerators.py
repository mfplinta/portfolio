from imagekit import ImageSpec, register
from imagekit.processors import ResizeToFill

PROJECT_THUMBNAIL_SIZE = (280, 160)

class ProjectThumbnail(ImageSpec):
    processors = [ResizeToFill(PROJECT_THUMBNAIL_SIZE[0], PROJECT_THUMBNAIL_SIZE[1])]
    format = 'jpeg'
    options = {'quality': 60}


class ProjectThumbnailWebp(ProjectThumbnail):
    format = 'webp'

class ProjectThumbnail2x(ProjectThumbnail):
    processors = [ResizeToFill(PROJECT_THUMBNAIL_SIZE[0]*2, PROJECT_THUMBNAIL_SIZE[1]*2)]

class ProjectThumbnailWebp2x(ProjectThumbnailWebp):
    processors = [ResizeToFill(PROJECT_THUMBNAIL_SIZE[0]*2, PROJECT_THUMBNAIL_SIZE[1]*2)]


register.generator('main:project_thumbnail', ProjectThumbnail)
register.generator('main:project_thumbnail2x', ProjectThumbnail2x)
register.generator('main:project_thumbnail_webp', ProjectThumbnailWebp)
register.generator('main:project_thumbnail_webp2x', ProjectThumbnailWebp2x)
