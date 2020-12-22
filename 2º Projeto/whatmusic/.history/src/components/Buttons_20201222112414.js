import React from "react";
// reactstrap components
import { Button } from "reactstrap";

class Buttons extends React.Component {
  render() {
    return (
      <>
        <Button color="primary" size="lg" type="button">
          Large button
        </Button>
        <Button color="secondary" size="lg" type="button">
          Large button
        </Button>
      </>
    );
  }
}

export default Buttons;