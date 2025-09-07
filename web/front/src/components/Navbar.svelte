<style>
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #F08787;
  border-radius: 10px;
}

ul li {
  float: left;
}

ul li a,form{
  display: block;
  color: #001200;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

input {
  background-color: #EBD9D1;
  border-radius: 10px;
}

ul li a:hover {
  background-color: #FFC7A7;
}
</style>
<ul>
  <li><a href="/">home</a></li>
  <li><a href="/famous">famous</a></li>
  <li><a href="/about">about</a></li>
  <li><a href="/random">random</a></li>
  <li>
    <form action="/action_page.php">
      <input placeholder="search" type="search" id="gsearch" name="gsearch">
      <input type="submit">
    </form></li>
</ul>

