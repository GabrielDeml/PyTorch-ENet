import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while(True):
  _, image = cap.read()
  # image = image.to(device)
  cv2.imshow("k",image)
  if cv2.waitKey(20) & 0xFF==ord('q'):
    break
cap.release()
cv2.destroyAllWindows()



# # video
# cap = cv2.VideoCapture("/content/sample_data/Drive1686.mp4")
# while(True):
#     _, image = cap.read()
#     start_time = time.time()
#     image = torch.from_numpy(image)
#     # image = image.unsqueeze(0)
#     prediction = model(image)
#     _, predictions = torch.max(prediction, 1)
#     print("\nPrediction time: {0:.4f} seconds".format(time.time() - start_time))
#     label_to_rgb = transforms.Compose([
#     ext_transforms.LongTensorToRGBPIL(class_encoding),
#     transforms.ToTensor()
#      ])
#     color_predictions = utils.batch_transform(predictions.cpu(), label_to_rgb)
#     utils.imshow_batch(image.data.cpu(), color_predictions)
#     # save_image(color_predictions, 'predictions_{0}.png'.format(time.time()))
# cap.release()