# social_network
IITU Final Project [ NSA4: Networking and Security (SDP9) (c.w.) (Алшынов Ш.К.) ]
<br>
Models:
  Follower |  (id, follower, following)<br>
  Post |      (id, user, content, created_at)<br>
  Like |      (id, user, post)<br>
  Comment |   (id, user, post, content)<br>
  Message |   (id, sender, recipient, message, created_at)<br>
<hr>
Endpoints:
<br>
  for authorization and authentication djoser package is used<br>
  GET |  'followers/'       | lists followers<br>
  GET |  'following/'       | lists following users<br>
  GET |  'posts/<int:pk>'   | lists user posts<br>
  POST | 'like/'            | like user post<br>
  GET |  'comments/<int:pk>'| list comments of post<br>
  GET |  'posts/'           | list request.user posts<br>
  POST | 'post/'            | create a post  <br>
  POST | 'follow/'          | follow user<br>
  POST | 'unfollow/'        | unfollow user<br>
  GET/POST | 'chat/'        | list messages/send message to user<br>
  GET |  'chat/<int:user>'  | list messages with request.user and user<br>
  GET |  'search/',         | search user by username<br>
