from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.module_item import ModuleItem
from app.models.estimate import Estimate
from app.models.estimate_item import EstimateItem
from app.schemas.estimate_schema import EstimateCreate
from app.core.dependencies import get_current_user

router = APIRouter(prefix="/api/estimate", tags=["Cost Estimation"])

@router.post("/")
def calculate_estimate(
    data: EstimateCreate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    items = db.query(ModuleItem).filter(
        ModuleItem.id.in_(data.module_item_ids)
    ).all()

    total = sum(item.price for item in items if item.price)

    estimate = Estimate(user_id=user.id, total_cost=total)
    db.add(estimate)
    db.commit()
    db.refresh(estimate)

    for item in items:
        estimate_item = EstimateItem(
            estimate_id=estimate.id,
            module_item_id=item.id,
            price=item.price
        )
        db.add(estimate_item)

    db.commit()

    return {
        "estimate_id": estimate.id,
        "total_cost": total
    }


@router.get("/{estimate_id}")
def get_estimate(estimate_id: int, db: Session = Depends(get_db)):
    estimate = db.query(Estimate).filter(Estimate.id == estimate_id).first()
    items = db.query(EstimateItem).filter(
        EstimateItem.estimate_id == estimate_id
    ).all()

    return {
        "total_cost": estimate.total_cost,
        "items": items
    }