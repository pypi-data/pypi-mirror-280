
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinncode.com

## IMPORTS
## MODULE UPDATED TO USE QT.PY
from qtpy.QtCore import Qt, QEasingCurve, QPoint, Slot, QParallelAnimationGroup, QPropertyAnimation, QAbstractAnimation, QTimeLine
from qtpy.QtGui import QPainter, QPixmap
from qtpy.QtWidgets import QStackedWidget, QWidget, QGraphicsOpacityEffect


"""
This is an extension of QStackedWidget which adds transition animation
And Navigation Functions to
your QStackedWidget widgets
You can customize the animations using a JSon file or Python statements
"""

## QStackedWidget Class
class QCustomQStackedWidget(QStackedWidget):
    def __init__(self, parent=None):
        super(QCustomQStackedWidget, self).__init__(parent)
        ## Initialize Default Values
        # Fade transition
        self.fadeTransition = False
        # Slide transition
        self.slideTransition = False
        # Default transition direction
        self.transitionDirection = Qt.Vertical
        # Default transition animation time
        self.transitionTime = 500
        # Default fade animation time
        self.fadeTime = 500
        # Default transition animation easing curve
        self.transitionEasingCurve = QEasingCurve.OutBack
        # Default transition animation easing curve
        self.fadeEasingCurve = QEasingCurve.Linear
        # Default current widget index
        self.currentWidget = 0
        # Default next widget index
        self.nextWidget = 0
        # Default widget position
        self._currentWidgetPosition = QPoint(0, 0)
        # Default boolean for active widget
        self.widgetActive = False


    
    ## Function to update transition direction
    def setTransitionDirection(self, direction):
        self.transitionDirection = direction
    
    ## Function to update transition speed
    def setTransitionSpeed(self, speed):
        self.transitionTime = speed

    
    ## Function to update fade speed
    def setFadeSpeed(self, speed):
        self.fadeTime = speed

    
    ## Function to update transition easing curve
    def setTransitionEasingCurve(self, aesingCurve):
        self.transitionEasingCurve = aesingCurve

    
    ## Function to update fade easing curve
    def setFadeCurve(self, aesingCurve):
        self.fadeEasingCurve = aesingCurve

    
    ## Function to update fade animation playing state
    def setFadeTransition(self, fadeState):
        if isinstance(fadeState, bool):
            self.fadeTransition = fadeState
        else:
            raise Exception("setFadeTransition() only accepts boolean variables")

    
    ## Function to update slide  playing state
    def setSlideTransition(self, slideState):
        if isinstance(slideState, bool):
            self.slideTransition = slideState
        else:
            raise Exception("setSlideTransition() only accepts boolean variables")

    
    ## Function to transition to previous widget
    @Slot()
    def slideToPreviousWidget(self):
        currentWidgetIndex = self.currentIndex()
        if currentWidgetIndex > 0:
            self.slideToWidgetIndex(currentWidgetIndex - 1)

    
    ## Function to transition to next widget
    @Slot()
    def slideToNextWidget(self):
        currentWidgetIndex = self.currentIndex()
        if currentWidgetIndex < (self.count() - 1):
            self.slideToWidgetIndex(currentWidgetIndex + 1)


    
    ## Function to transition to a given widget index
    def slideToWidgetIndex(self, index):
        if index > (self.count() - 1):
            index = index % self.count()
        elif index < 0:
            index = (index + self.count()) % self.count()
        if self.slideTransition:
            self.slideToWidget(self.widget(index))
        else:
            self.setCurrentIndex(index)

    
    ## Function to transition to a given widget
    def slideToWidget(self, newWidget):
        # If the widget is active, exit the function
        if self.widgetActive:
            return

        # Update widget active bool
        self.widgetActive = True

        # Get current and next widget index
        _currentWidgetIndex = self.currentIndex()
        _nextWidgetIndex = self.indexOf(newWidget)

        # If current widget index is equal to next widget index, exit function
        if _currentWidgetIndex == _nextWidgetIndex:
            self.widgetActive = False
            return

        anim_group = QParallelAnimationGroup(
            self, finished=self.animationDoneSlot
        )

        # Get X and Y position of QStackedWidget
        offsetX, offsetY = self.frameRect().width(), self.frameRect().height()
        # Set the next widget geometry
        self.widget(_nextWidgetIndex).setGeometry(self.frameRect())

        self.widget(_nextWidgetIndex).show()
        self.widget(_nextWidgetIndex).raise_()

        if self.slideTransition:
            # Animate transition
            # Set left right(horizontal) or up down(vertical) transition
            if not self.transitionDirection == Qt.Horizontal:
                if _currentWidgetIndex < _nextWidgetIndex:
                    # Down up transition
                    offsetX, offsetY = 0, -offsetY
                else:
                    # Up down transition
                    offsetX = 0
            else:
                # Right left transition
                if _currentWidgetIndex < _nextWidgetIndex:
                    offsetX, offsetY = -offsetX, 0
                else:
                    # Left right transition
                    offsetY = 0

            nextWidgetPosition = self.widget(_nextWidgetIndex).pos()
            currentWidgetPosition = self.widget(_currentWidgetIndex).pos()
            self._currentWidgetPosition = currentWidgetPosition

            offset = QPoint(offsetX, offsetY)
            self.widget(_nextWidgetIndex).move(nextWidgetPosition - offset)
            
            for index, start, end in zip(
                (_currentWidgetIndex, _nextWidgetIndex),
                (currentWidgetPosition, nextWidgetPosition - offset),
                (currentWidgetPosition + offset, nextWidgetPosition)
            ):
                animation = QPropertyAnimation(
                    self.widget(index),
                    b"pos",
                    duration=self.transitionTime,
                    easingCurve=self.transitionEasingCurve,
                    startValue=start,
                    endValue=end,
                )
                anim_group.addAnimation(animation)

        # Play fade animation
        if self.fadeTransition:
            opacityEffect = QGraphicsOpacityEffect(self.widget(self.currentWidget))
            self.setGraphicsEffect(opacityEffect)
            opacityAni = QPropertyAnimation(opacityEffect, b'opacity', self.widget(self.currentWidget))
            opacityAni.setStartValue(0)
            opacityAni.setEndValue(1)
            opacityAni.setDuration(self.fadeTime)
            opacityAni.setEasingCurve(self.fadeEasingCurve)
            opacityAni.finished.connect(opacityEffect.deleteLater)
            # opacityAni.start()

            anim_group.addAnimation(opacityAni)

        self.nextWidget = _nextWidgetIndex
        self.currentWidget = _currentWidgetIndex
        
        self.widgetActive = True
        # self.setCurrentIndex(self.nextWidget)
        anim_group.start(QAbstractAnimation.DeleteWhenStopped)

    
    ## Function to hide old widget and show new widget after animation is done
    @Slot()
    def animationDoneSlot(self):
        # self.widget(self.currentWidget).hide()
        self.setCurrentIndex(self.nextWidget)
        self.widget(self.currentWidget).move(self._currentWidgetPosition)
        self.widgetActive = False

    
    ## Function extending the QStackedWidget setCurrentWidget to animate transition
    @Slot()
    def setCurrentWidget(self, widget):
        currentIndex = self.currentIndex()
        nextIndex = self.indexOf(widget)
        if currentIndex == nextIndex and self.currentWidget == currentIndex:
            return
        
        # FadeWidgetTransition(self, self.widget(self.currentIndex()), self.widget(self.indexOf(widget)))
        self.slideToWidget(widget)
        # if not self.slideTransition:
        #     self.setCurrentIndex(0)
            
        if not self.slideTransition and not self.fadeTransition:
            self.setCurrentIndex(nextIndex)

