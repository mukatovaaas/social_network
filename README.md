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
  get |  'followers/'       | lists followers<br>
  get |  'following/'       | lists following users<br>
  get |  'posts/<int:pk>'   | lists user posts<br>
  post | 'like/'            | like user post<br>
  get |  'comments/<int:pk>'| list comments of post<br>
  get |  'posts/'           | list request.user posts<br>
  post | 'post/'            | create a post  <br>
  post | 'follow/'          | follow user<br>
  post | 'unfollow/'        | unfollow user<br>
  get/post | 'chat/'        | list messages/send message to user<br>
  get |  'chat/<int:user>'  | list messages with request.user and user<br>
  get |  'search/',         | search user by username<br>
