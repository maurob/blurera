def temporal_filter(n_frames):
    history = []
    img, bboxes = yield
    while True:
        try:
            img_1, bboxes_1 = history[-1]
        except IndexError:
            pass
        else:
            if not bboxes_1 and bboxes:
                history = [im,bboxes for im,_ in history]
            elif bboxes_1 and not bboxes:
                pass
            else:
                pass

        history.append(img, bboxes)
        if len(history) > n_frames:
            img, bboxes = yield history.pop(0)



class TemporalExtendedFilter:
    def __init__(self, n_frames):
        self.n_frames = 10
        self.states =
    def __call__(self, img, bboxes):

        return img, bboxes

