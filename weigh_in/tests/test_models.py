from datetime import date, datetime, timedelta

from ..core.models import Entry, Log


def test_log(client, db):
    log = Log(
        name='test',
        email='test@test.com',
        guid='123'
    )
    assert str(log) == 'test'


def test_measurement(client, db):
    log = Log(
        name='test',
        email='test@test.com',
        guid='123'
    )
    entry = Entry(
        measured_on=date.today(),
        pounds=123,
        log=log
    )
    log.entries.append(entry)
    db.session.add(log)
    db.session.commit()
    assert entry.id
    assert str(entry) == datetime.strftime(
        entry.measured_on, '%Y-%m-%d')
    assert log.last_weight() == 123
    assert log.next_date() == date.today() + timedelta(days=1)
